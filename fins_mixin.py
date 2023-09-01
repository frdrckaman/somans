import os
import sqlite3
from sqlite3 import Error
import env_mixin


def read_log_file():
    txt_data = []
    with open(env_mxin.FIN_SERVICE_FILE, 'r') as file:
        for file_line in file.readlines():
            txt_data.append(file_line.replace(" ", ""))
    return txt_data


def read_log_file_node1():
    txt_data = []
    if os.path.isfile(env_mxin.FIN_SERVICE_FILE_NODE1):
        if os.path.isfile(f"{env_mxin.FIN_NODE1_DIR}finservices_n1.txt"):
            os.remove(f"{env_mxin.FIN_NODE1_DIR}finservices_n1.txt")
        with open(env_mxin.FIN_SERVICE_FILE_NODE1, 'r') as file:
            for file_line in file.readlines():
                txt_data.append(file_line.replace(" ", ""))
        os.rename(env_mxin.FIN_SERVICE_FILE_NODE1, f'{env_mxin.FIN_NODE1_DIR}finservices_n1.txt')
    elif os.path.isfile(f"{env_mxin.FIN_NODE1_DIR}finservices_n1.txt"):
        with open(f"{env_mxin.FIN_NODE1_DIR}finservices_n1.txt", 'r') as file:
            for file_line in file.readlines():
                txt_data.append(file_line.replace(" ", ""))
    return txt_data


def read_log_file_node2():
    txt_data = []
    if os.path.isfile(env_mxin.FIN_SERVICE_FILE_NODE2):
        if os.path.isfile(f"{env_mxin.FIN_NODE2_DIR}finservices_n2.txt"):
            os.remove(f"{env_mxin.FIN_NODE2_DIR}finservices_n2.txt")
        with open(env_mxin.FIN_SERVICE_FILE_NODE2, 'r') as file:
            for file_line in file.readlines():
                txt_data.append(file_line.replace(" ", ""))
        os.rename(env_mxin.FIN_SERVICE_FILE_NODE2, f'{env_mxin.FIN_NODE2_DIR}finservices_n2.txt')
    elif os.path.isfile(f"{env_mxin.FIN_NODE2_DIR}finservices_n2.txt"):
        with open(f"{env_mxin.FIN_NODE2_DIR}finservices_n2.txt", 'r') as file:
            for file_line in file.readlines():
                txt_data.append(file_line.replace(" ", ""))
    return txt_data


# def fin_services_status():
#     service_status_data = []
#     service_status = read_log_file()
#     for fin in range(4, 26):
#         service = service_status[fin].split('|')
#         service_stat = service[3].split(';')
#         service_stat1 = service_stat[1].replace('1m', '')
#         service_status_data.append(service_stat1)
#     return service_status_data

def fin_services_status_node1():
    service_status_data = []
    service_status = read_log_file_node1()
    for fin in range(4, 24):
        service = service_status[fin].split('|')
        service_stat = service[3].split(';')
        service_stat1 = service_stat[1].replace('1m', '')
        service_status_data.append(service_stat1)
    return service_status_data


def fin_services_status_node2():
    service_status_data = []
    service_status = read_log_file_node2()
    for fin in range(4, 24):
        service = service_status[fin].split('|')
        service_stat = service[3].split(';')
        service_stat1 = service_stat[1].replace('1m', '')
        service_status_data.append(service_stat1)
    return service_status_data


def db():
    return f"{env_mxin.FIN_SQLITE_DB}"


def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(db())
    except Error as e:
        print(e)
    return conn


# def run_job():
#     service_log = read_log_file()[2].split('|')
#     service_log1 = service_log[1].replace('FinacleServicesAdministration', '')
#     show_service_time = f'{service_log1[:3]} {service_log1[3:6]} {service_log1[6:8]} {service_log1[8:16]} {service_log1[16:19]} {service_log1[19:]}'
#     print(show_service_time)
#     fin_status = fin_services_status()
#     conn = create_connection()
#     cur = conn.cursor()
#     cur.execute(f"DELETE FROM {env_mxin.FIN_SQLITE_TABLE}")
#     cur.execute(f"UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = '{env_mxin.FIN_SQLITE_TABLE}'")
#     sql_insert = f"INSERT INTO fins_dashboard_finservices (ConfigService, FINRPT_finlstclnt,FINRPT_comnclnt,CBC,Finlistval,Coresession,Referral,Uniser_TZ,MQMSwiftIn_TZ,MQMSwiftOut_TZ,MQMRtgsIn_TZ,MQMRtgsOut_TZ,MQMRead_TZ,Dispatcher_TZ,Binagent_TZ,Swiftsrv_TZ,Pmssrv_TZ,Genlimo_TZ,Aabsrv_TZ,Eabgst_TZ,Trswift_TZ,Uplpsmsg_TZ,fin_timestamp) VALUES ('{fin_status[0]}', '{fin_status[1]}', '{fin_status[2]}', '{fin_status[3]}', '{fin_status[4]}', '{fin_status[5]}', '{fin_status[6]}', '{fin_status[7]}', '{fin_status[8]}', '{fin_status[9]}', '{fin_status[10]}', '{fin_status[11]}', '{fin_status[12]}', '{fin_status[13]}',' {fin_status[14]}', '{fin_status[15]}', '{fin_status[16]}', '{fin_status[17]}', '{fin_status[18]}', '{fin_status[19]}', '{fin_status[20]}', '{fin_status[21]}', '{show_service_time}')"
#     cur.execute(sql_insert)
#     conn.commit()
#     conn.close()

def run_job_node1():
    service_log = read_log_file_node1()[2].split('|')
    service_log1 = service_log[1].replace('FinacleServicesAdministration', '')
    show_service_time = f'{service_log1[:3]} {service_log1[3:6]} {service_log1[6:8]} {service_log1[8:16]} {service_log1[16:19]} {service_log1[19:]}'
    print(show_service_time)
    fin_status = fin_services_status_node1()
    conn = create_connection()
    cur = conn.cursor()
    cur.execute(f"DELETE FROM {env_mxin.FIN_SQLITE_TABLE}")
    cur.execute(f"UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = '{env_mxin.FIN_SQLITE_TABLE}'")
    sql_insert = f"INSERT INTO {env_mxin.FIN_SQLITE_TABLE} (ConfigService, FINRPT_finlstclnt,FINRPT_comnclnt,CBC,Finlistval,Coresession,Referral,Uniser_TZ,MQMSwiftIn_TZ,MQMSwiftOut_TZ,MQMRtgsIn_TZ,MQMRtgsOut_TZ,MQMRead_TZ,Dispatcher_TZ,Binagent_TZ,Swiftsrv_TZ,Pmssrv_TZ,Genlimo_TZ,Aabsrv_TZ,Eabgst_TZ,fin_timestamp,node) VALUES ('{fin_status[0]}', '{fin_status[1]}', '{fin_status[2]}', '{fin_status[3]}', '{fin_status[4]}', '{fin_status[5]}', '{fin_status[6]}', '{fin_status[7]}', '{fin_status[8]}', '{fin_status[9]}', '{fin_status[10]}', '{fin_status[11]}', '{fin_status[12]}', '{fin_status[13]}','{fin_status[14]}', '{fin_status[15]}', '{fin_status[16]}', '{fin_status[17]}', '{fin_status[18]}', '{fin_status[19]}', '{show_service_time}', 1)"
    cur.execute(sql_insert)
    conn.commit()
    conn.close()


def run_job_node2():
    service_log = read_log_file_node2()[2].split('|')
    service_log1 = service_log[1].replace('FinacleServicesAdministration', '')
    show_service_time = f'{service_log1[:3]} {service_log1[3:6]} {service_log1[6:8]} {service_log1[8:16]} {service_log1[16:19]} {service_log1[19:]}'
    print(show_service_time)
    fin_status = fin_services_status_node2()
    conn = create_connection()
    cur = conn.cursor()
    # cur.execute(f"DELETE FROM {env_mxin.FIN_SQLITE_TABLE}")
    # cur.execute(f"UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = '{env_mxin.FIN_SQLITE_TABLE}'")
    sql_insert = f"INSERT INTO {env_mxin.FIN_SQLITE_TABLE} (ConfigService, FINRPT_finlstclnt,FINRPT_comnclnt,CBC,Finlistval,Coresession,Referral,Uniser_TZ,MQMSwiftIn_TZ,MQMSwiftOut_TZ,MQMRtgsIn_TZ,MQMRtgsOut_TZ,MQMRead_TZ,Dispatcher_TZ,Binagent_TZ,Swiftsrv_TZ,Pmssrv_TZ,Genlimo_TZ,Aabsrv_TZ,Eabgst_TZ,fin_timestamp,node) VALUES ('{fin_status[0]}', '{fin_status[1]}', '{fin_status[2]}', '{fin_status[3]}', '{fin_status[4]}', '{fin_status[5]}', '{fin_status[6]}', '{fin_status[7]}', '{fin_status[8]}', '{fin_status[9]}', '{fin_status[10]}', '{fin_status[11]}', '{fin_status[12]}', '{fin_status[13]}','{fin_status[14]}', '{fin_status[15]}', '{fin_status[16]}', '{fin_status[17]}', '{fin_status[18]}', '{fin_status[19]}', '{show_service_time}', 2)"
    cur.execute(sql_insert)
    conn.commit()
    conn.close()


def run_job():
    run_job_node1()
    run_job_node2()


def main():
    run_job()


if __name__ == '__main__':
    main()
