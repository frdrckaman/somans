import re
import os
import shutil
import pandas as pd
from datetime import datetime
import env_mixin

logfile = f'{env_mixin.IDAP_LOGS_DIR}somans.log'
logger = env_mixin.logservice.setup_logger('svr_sft', logfile)

logVar = {'project_name': 'SOMANS', 'report_tag': 'svr_sft', 'status': 'Success', 'job_date': datetime.today().strftime('%Y-%m-%d'),
          'job_timestamp': datetime.today().strftime('%Y-%m-%d %H:%M')}
dfLog = pd.DataFrame(logVar, index=[0])

try:
    myQuery = pd.read_csv(env_mixin.SOMANS_SFTWR_SVRS_DATA)
    df = myQuery
    msg0 = 'Sever Software data fetched Successful'
    logger.info(msg0)
    dfLog['report_date'] = datetime.today().strftime('%Y-%m-%d')
    dfLog['status'] = 'Success'
    dfLog['job_output'] = msg0
    dfLog.to_sql(env_mixin.IDAP_LOG_TBL, env_mixin.engine_idap, if_exists='append', index=False)
    try:
        df.to_sql(env_mixin.SOMANS_SFTWR_SVRS, env_mixin.engine_idap, if_exists='append', index=False)
        msg1 = 'Sever Software data inserted Successful'
        logger.info(msg1)
        dfLog['status'] = 'Success'
        dfLog['job_output'] = msg1
        dfLog.to_sql(env_mixin.IDAP_LOG_TBL, env_mixin.engine_idap, if_exists='append', index=False)
        try:
            df['job_date'] = datetime.today().strftime('%Y-%m-%d')
            df['job_timestamp'] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            df.to_sql(env_mixin.SOMANS_SFTWR_SVRS_HIST,  env_mixin.engine_idap, if_exists='append', index=False)
            msg2 = 'Sever Software history data inserted Successful'
            logger.info(msg1)
            dfLog['status'] = 'Success'
            dfLog['job_output'] = msg2
            dfLog.to_sql(env_mixin.IDAP_LOG_TBL, env_mixin.engine_idap, if_exists='append', index=False)
            try:
                os.rename(f'{env_mixin.SOMANS_SCCM_DIR}List_of_Applications_Server.csv',
                          f"{env_mixin.SOMANS_SCCM_DIR}List_of_Applications_Server{datetime.today().strftime('%Y-%m-%d')}.csv")
                shutil.move(f"{env_mixin.SOMANS_SCCM_DIR}List_of_Applications_Server{datetime.today().strftime('%Y-%m-%d')}.csv",
                            f"{env_mixin.SOMANS_ARCHIVE_DIR}List_of_Applications_Server{datetime.today().strftime('%Y-%m-%d')}.csv")
                msg3 = 'List_of_Applications_Server archived Successful'
                logger.info(msg1)
                dfLog['status'] = 'Success'
                dfLog['job_output'] = msg3
                dfLog.to_sql(env_mixin.IDAP_LOG_TBL, env_mixin.engine_idap, if_exists='append', index=False)
            except Exception as e3:
                dfLog['status'] = 'Error'
                dfLog['job_output'] = re.sub('\W+', ' ', str(e3))
                dfLog.to_sql(env_mixin.IDAP_LOG_TBL, env_mixin.engine_idap, if_exists='append', index=False)
                logger.error(e3)
                raise SystemExit(e3)
        except Exception as e2:
            dfLog['status'] = 'Error'
            dfLog['job_output'] = re.sub('\W+', ' ', str(e2))
            dfLog.to_sql(env_mixin.IDAP_LOG_TBL, env_mixin.engine_idap, if_exists='append', index=False)
            logger.error(e2)
            raise SystemExit(e2)
    except Exception as e1:
        dfLog['status'] = 'Error'
        dfLog['job_output'] = re.sub('\W+', ' ', str(e1))
        dfLog.to_sql(env_mixin.IDAP_LOG_TBL, env_mixin.engine_idap, if_exists='append', index=False)
        logger.error(e1)
        raise SystemExit(e1)
except Exception as e0:
    dfLog['status'] = 'Error'
    dfLog['job_output'] = re.sub('\W+', ' ', str(e0))
    dfLog.to_sql(env_mixin.IDAP_LOG_TBL, env_mixin.engine_idap, if_exists='append', index=False)
    logger.error(e0)
    raise SystemExit(e0)
