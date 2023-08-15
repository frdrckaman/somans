import pandas as pd
import os
import re
import glob
from datetime import datetime
import sqlalchemy
from sqlalchemy.engine import URL
from sqlalchemy import create_engine
import warnings
import env_mxin
import logservice


warnings.filterwarnings('ignore')

if env_mxin.DATABASE_SQLITE_ENABLED:
    # sqlite db for testing
    engine = sqlalchemy.create_engine('sqlite:///C:/Users/A248080/PycharmProjects/somans/db.sqlite3')
else:
    # sql server db
    connection_string = 'DRIVER={' + env_mxin.IDAP_DB_DRIVER + '};SERVER=' + env_mxin.IDAP_CLUSTER + ';DATABASE=' + env_mxin.IDAP_DB + ';ENCRYPT=yes;TrustServerCertificate=Yes;MultiSubnetFailover=Yes;UID=' + env_mxin.IDAP_USER + ';PWD=' + env_mxin.IDAP_PWD
    connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
    engine = create_engine(connection_url)

# insert log to a file
logfile = f'{env_mxin.IDAP_POS_LOGS}pos.log'
logger = logservice.setup_logger(env_mxin.IDAP_POS_TAG, logfile)

# insert logs to database
logVar = {'project_name': 'POS', 'report_date': datetime.today().strftime('%Y-%m-%d'), 'report_tag': env_mxin.IDAP_POS_TAG, 'status': 'Success', 'job_date': datetime.today().strftime('%Y-%m-%d'),
          'job_timestamp': datetime.today().strftime('%Y-%m-%d %H:%M:%S')}
dfLog = pd.DataFrame(logVar, index=[0])

# Set the folder path where the files are located
folder_path = env_mxin.IDAP_POS_DT_DIR

# Get the current date
current_date = datetime.now().date()
current_month = datetime.now().strftime('%Y%m')
today_date = datetime.now().strftime('%d')

# define the search pattern for the files
search_pattern = os.path.join(folder_path, f'DA15[48]*{current_month}*.txt')

# Find al matching files in the folder
matching_files = glob.glob(search_pattern)

# Output file name
output_file = f"{env_mxin.IDAP_POS_OUTPUT_DIR}POS Statement as of {current_date}.xlsx"

# Create an empty dataframe
df = pd.DataFrame(
    columns=['merchant', 'tran_date', 'transaction_time', 'date_transferred', 'pos_number', 'location', 'card_number',
             'currency', 'gross_value', 'commission', 'net_value'])

dff = []

# Loop through each file and process
if matching_files:

    for file_path in matching_files:

        # Read the text file
        with open(file_path, 'r') as file:
            lines = file.readlines()

        digits = file_path.split('_')[1][:8]

        # tranferred_date = digits
        try:
            tranferred_date = pd.to_datetime(digits, format="%Y%m%d").strftime("%d %b %Y")
        except ValueError:
            tranferred_date = "Invalid Date"

        file_name = os.path.basename(file_path)

        if file_name.startswith('DA154'):
            currency = 'TZS'
        else:
            currency = 'USD'

        # initialise variables
        merchant_number = None
        prod_date = None
        is_inside_block = False

        # Process each line and populate the DataFrame
        for line in lines[1:]:
            line = line.strip()

            if line.startswith('MERCHANT NO :'):
                merchant_number = line.split(':')[1].strip()[:12]
                is_inside_block = True
                continue

            if line == 'END OF REPORT':
                is_inside_block = False

            if is_inside_block:

                if line.startswith('ADDRESS     :'):
                    location = line.split(':')[1].strip()[:35]

                pos_number = line[14:24].strip()

                # date_month = line[0:5] + f"/2023"
                date_month = line[0:5] + f"/{datetime.now().year}"

                try:
                    tran_date = pd.to_datetime(date_month, format="%d/%m/%Y").strftime("%d %b %Y")
                except ValueError:
                    tran_date = "Invalid Date"

                Tran_Time = line[6:14].strip()

                card_number = line[36:51].strip()

                try:
                    gross_value = float(line[98:110])
                except ValueError:
                    gross_value = 0

                commission = gross_value * 0.0177

                net_value = gross_value - commission

                data = [merchant_number, tran_date, Tran_Time, tranferred_date, pos_number, location, card_number,
                        currency, gross_value, commission, net_value]

                row = pd.Series(data, index=df.columns)

                dff.append(row)

dff1 = pd.DataFrame(dff)
dff1['job_date'] = datetime.today().strftime('%Y-%m-%d')
dff1['job_timestamp'] = datetime.today().strftime('%Y-%m-%d  %H:%M:%S')
df2 = dff1[(dff1['tran_date'] != 'Invalid Date') & (dff1['pos_number'] != '')]

try:
    df2.to_sql(env_mxin.IDAP_POS_TBL, engine, if_exists='append', index=False)
    logger.info("Data inserted successful")
    try:
        dfLog['status'] = 'Success'
        dfLog['job_output'] = 'Data inserted successful'
        dfLog.to_sql(env_mxin.IDAP_LOG_TBL, engine, if_exists='append', index=False)
    except Exception as e2:
        dfLog['status'] = 'Error'
        dfLog['job_output'] = re.sub('\W+', ' ', str(e2))
        dfLog.to_sql(env_mxin.IDAP_LOG_TBL, engine, if_exists='append', index=False)
        raise SystemExit(e2)
except Exception as e1:
    dfLog['status'] = 'Error'
    dfLog['job_output'] = re.sub('\W+', ' ', str(e1))
    dfLog.to_sql(env_mxin.IDAP_LOG_TBL, engine, if_exists='append', index=False)
    raise SystemExit(e1)
