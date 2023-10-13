import sqlite3
from sqlite3 import Error
import env_mixin
from glob import iglob
from os import path
from datetime import datetime
import logservice
import pyodbc


def db():
    return f"{env_mixin.FIN_SQLITE_DB}"


def create_connection():
    conn = None
    try:
        cnxn = pyodbc.connect(env_mixin.connection_string_idap)
        conn = cnxn.cursor()
        # conn = sqlite3.connect(db())
    except Error as e:
        print(e)
    return conn


def get_service(fpath):
    return [path.basename(f)[:-4] for f in iglob(fpath + "*.txt")]


def node1_service_status(fpath):
    status = []
    for fin in env_mixin.FIN_SERVICES.split(','):
        status.append('UP') if fin in get_service(fpath) else status.append('DOWN')
    return status


def node2_service_status(fpath):
    status = []
    for fin in env_mixin.FIN_SERVICES.split(','):
        status.append('UP') if fin in get_service(fpath) else status.append('DOWN')
    return status


def update_node1():
    stat = node1_service_status(env_mixin.FIN_SERVICE_FILE_NODE1)
    timestamp = str(datetime.now())
    stat.append(timestamp)
    stat.append(1)
    status = tuple(stat)
    conn = create_connection()
    # cur = conn.cursor()
    conn.execute(f"DELETE FROM {env_mixin.FIN_SERVICE_TABLE}")
    conn.execute(f"DBCC CHECKIDENT ('{env_mixin.FIN_SERVICE_TABLE}', RESEED, 0)")
    # conn.execute(f"UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = '{env_mixin.FIN_SERVICE_TABLE}'")
    sql_insert = f"INSERT INTO {env_mixin.FIN_SERVICE_TABLE} (ConfigService, FINRPT_finlstclnt,FINRPT_comnclnt,CBC,Finlistval,Coresession,Referral,Uniser_TZ,MQMSwiftIn_TZ,MQMSwiftOut_TZ,MQMRtgsIn_TZ,MQMRtgsOut_TZ,MQMRead_TZ,Dispatcher_TZ,Binagent_TZ,Swiftsrv_TZ,Pmssrv_TZ,Genlimo_TZ,Aabsrv_TZ,Eabgst_TZ,Trswift_TZ,Uplpsmsg_TZ,fin_timestamp,node) VALUES {status}"
    sql_insert_hist = f"INSERT INTO {env_mixin.FIN_TABLE_HIST} (ConfigService, FINRPT_finlstclnt,FINRPT_comnclnt,CBC,Finlistval,Coresession,Referral,Uniser_TZ,MQMSwiftIn_TZ,MQMSwiftOut_TZ,MQMRtgsIn_TZ,MQMRtgsOut_TZ,MQMRead_TZ,Dispatcher_TZ,Binagent_TZ,Swiftsrv_TZ,Pmssrv_TZ,Genlimo_TZ,Aabsrv_TZ,Eabgst_TZ,Trswift_TZ,Uplpsmsg_TZ,fin_timestamp,node) VALUES {status}"
    conn.execute(sql_insert)
    conn.execute(sql_insert_hist)
    conn.commit()
    conn.close()


def update_node2():
    stat = node2_service_status(env_mixin.FIN_SERVICE_FILE_NODE1)
    timestamp = str(datetime.now())
    stat.append(timestamp)
    stat.append(2)
    status = tuple(stat)
    conn = create_connection()
    # cur = conn.cursor()
    sql_insert = f"INSERT INTO {env_mixin.FIN_SERVICE_TABLE} (ConfigService, FINRPT_finlstclnt,FINRPT_comnclnt,CBC,Finlistval,Coresession,Referral,Uniser_TZ,MQMSwiftIn_TZ,MQMSwiftOut_TZ,MQMRtgsIn_TZ,MQMRtgsOut_TZ,MQMRead_TZ,Dispatcher_TZ,Binagent_TZ,Swiftsrv_TZ,Pmssrv_TZ,Genlimo_TZ,Aabsrv_TZ,Eabgst_TZ,Trswift_TZ,Uplpsmsg_TZ,fin_timestamp,node) VALUES {status}"
    sql_insert_hist = f"INSERT INTO {env_mixin.FIN_TABLE_HIST} (ConfigService, FINRPT_finlstclnt,FINRPT_comnclnt,CBC,Finlistval,Coresession,Referral,Uniser_TZ,MQMSwiftIn_TZ,MQMSwiftOut_TZ,MQMRtgsIn_TZ,MQMRtgsOut_TZ,MQMRead_TZ,Dispatcher_TZ,Binagent_TZ,Swiftsrv_TZ,Pmssrv_TZ,Genlimo_TZ,Aabsrv_TZ,Eabgst_TZ,Trswift_TZ,Uplpsmsg_TZ,fin_timestamp,node) VALUES {status}"
    conn.execute(sql_insert)
    conn.execute(sql_insert_hist)
    conn.commit()
    conn.close()


def main():
    logfile = f'{env_mixin.FIN_SERVICES_LOGS}finservices.log'
    logger = logservice.setup_logger(env_mixin.FIN_SERVICES_TAG, logfile)

    print(env_mixin.FIN_SERVICE_FILE_NODE1)
    print(get_service(env_mixin.FIN_SERVICE_FILE_NODE1))

    try:
        update_node1()
        logger.info("Node 1 Finacle Services fetched Successful")
    except Exception as e1:
        logger.error(e1)
        raise SystemExit(e1)

    try:
        update_node2()
        logger.info("Node 2 Finacle Services fetched Successful")
    except Exception as e2:
        logger.error(e2)
        raise SystemExit(e2)


main()
