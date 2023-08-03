import os
import sqlite3
from sqlite3 import Error
import env_mxin
from glob import iglob
from os import path
from datetime import datetime


def db():
    return f"{env_mxin.FIN_SQLITE_DB}"


def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(db())
    except Error as e:
        print(e)
    return conn


def get_service(fpath):
    return [path.basename(f)[:-4] for f in iglob(fpath + "*.txt")]


def node1_service_status(fpath):
    status = []
    for fin in env_mxin.FIN_SERVICES.split(','):
        status.append('UP') if fin in get_service(fpath) else status.append('DOWN')
    return status


def node2_service_status(fpath):
    status = []
    for fin in env_mxin.FIN_SERVICES.split(','):
        status.append('UP') if fin in get_service(fpath) else status.append('DOWN')
    return status


def update_node1():
    stat = node1_service_status(env_mxin.FIN_SERVICE_FILE_NODE1)
    timestamp = str(datetime.now())
    stat.append(timestamp)
    stat.append(1)
    status = tuple(stat)
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(f"DELETE FROM {env_mxin.FIN_SQLITE_TABLE}")
    cur.execute(f"UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = '{env_mxin.FIN_SQLITE_TABLE}'")
    sql_insert = f"INSERT INTO {env_mxin.FIN_SQLITE_TABLE} (ConfigService, FINRPT_finlstclnt,FINRPT_comnclnt,CBC,Finlistval,Coresession,Referral,Uniser_TZ,MQMSwiftIn_TZ,MQMSwiftOut_TZ,MQMRtgsIn_TZ,MQMRtgsOut_TZ,MQMRead_TZ,Dispatcher_TZ,Binagent_TZ,Swiftsrv_TZ,Pmssrv_TZ,Genlimo_TZ,Aabsrv_TZ,Eabgst_TZ,fin_timestamp,node) VALUES {status}"
    cur.execute(sql_insert)
    conn.commit()
    conn.close()


# print(node1_service_status(env_mxin.FIN_SERVICE_FILE_NODE1))

update_node1()

def main():
    print(node1_service_status(env_mxin.FIN_SERVICE_FILE_NODE1))
    print(env_mxin.FIN_SERVICE_FILE_NODE1)
