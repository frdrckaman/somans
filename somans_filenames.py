import os
import re
import pandas as pd
from datetime import datetime
import env_mixin

logfile = f'{env_mixin.IDAP_LOGS_DIR}somans.log'
logger = env_mixin.logservice.setup_logger('bnch_srv_sft', logfile)

logVar = {'project_name': 'SOMANS', 'report_tag': 'sccm_files', 'status': 'Success', 'job_date': datetime.today().strftime('%Y-%m-%d'),
          'job_timestamp': datetime.today().strftime('%Y-%m-%d %H:%M')}
dfLog = pd.DataFrame(logVar, index=[0])

try:
    os.path.isfile(f"{env_mixin.SOMANS_SCCM_DIR}Tanzania - List of Applications per Server.csv")
    msg0 = 'Tanzania - List of Applications per Server file fetched Successful'
    logger.info(msg0)
    dfLog['report_date'] = datetime.today().strftime('%Y-%m-%d')
    dfLog['status'] = 'Success'
    dfLog['job_output'] = msg0
    dfLog.to_sql(env_mixin.IDAP_LOG_TBL, env_mixin.engine_idap, if_exists='append', index=False)
    try:
        os.path.isfile(f"{env_mixin.SOMANS_SCCM_DIR}Tanzania - List of Applications per Workstation.csv")
        msg1 = 'Tanzania - List of Applications per Workstation file fetched Successful'
        logger.info(msg1)
        dfLog['report_date'] = datetime.today().strftime('%Y-%m-%d')
        dfLog['status'] = 'Success'
        dfLog['job_output'] = msg1
        dfLog.to_sql(env_mixin.IDAP_LOG_TBL, env_mixin.engine_idap, if_exists='append', index=False)
        try:
            os.path.isfile(f"{env_mixin.SOMANS_SCCM_DIR}Tanzania - List of Servers csv.csv")
            msg2 = 'Tanzania - List of Servers file fetched Successful'
            logger.info(msg2)
            dfLog['report_date'] = datetime.today().strftime('%Y-%m-%d')
            dfLog['status'] = 'Success'
            dfLog['job_output'] = msg2
            dfLog.to_sql(env_mixin.IDAP_LOG_TBL, env_mixin.engine_idap, if_exists='append', index=False)
            try:
                os.path.isfile(f"{env_mixin.SOMANS_SCCM_DIR}Tanzania - List of Workstations csv.csv")
                msg3 = 'Tanzania - List of Workstations file fetched Successful'
                logger.info(msg3)
                dfLog['report_date'] = datetime.today().strftime('%Y-%m-%d')
                dfLog['status'] = 'Success'
                dfLog['job_output'] = msg3
                dfLog.to_sql(env_mixin.IDAP_LOG_TBL, env_mixin.engine_idap, if_exists='append', index=False)
                try:
                    os.rename(f'{env_mixin.SOMANS_SCCM_DIR}Tanzania - List of Applications per Server.csv',
                              f'{env_mixin.SOMANS_SCCM_DIR}List_of_Applications_Server.csv')
                    os.rename(f'{env_mixin.SOMANS_SCCM_DIR}Tanzania - List of Applications per Workstation.csv',
                              f'{env_mixin.SOMANS_SCCM_DIR}List_of_Applications_Workstation.csv')
                    os.rename(f'{env_mixin.SOMANS_SCCM_DIR}Tanzania - List of Servers csv.csv',
                              f'{env_mixin.SOMANS_SCCM_DIR}List_of_Servers.csv')
                    os.rename(f'{env_mixin.SOMANS_SCCM_DIR}Tanzania - List of Workstations csv.csv',
                              f'{env_mixin.SOMANS_SCCM_DIR}List_of_Workstations.csv')
                except Exception as e4:
                    dfLog['status'] = 'Error'
                    dfLog['job_output'] = re.sub('\W+', ' ', str(e4))
                    dfLog.to_sql(env_mixin.IDAP_LOG_TBL, env_mixin.engine_idap, if_exists='append', index=False)
                    logger.error(e4)
                    raise SystemExit(e4)
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

