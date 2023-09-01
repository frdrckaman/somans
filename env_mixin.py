from sqlalchemy.engine import URL
from sqlalchemy import create_engine
import os
from pathlib import Path
import environ
import logservice

ENV_DIR = str(".env")

env = environ.Env(
    DJANGO_DEBUG=(bool, False),
    DEBUG_TOOLBAR=(bool, False),
    DATABASE_SQLITE_ENABLED=(bool, False),
    DJANGO_EMAIL_ENABLED=(bool, False),
    FIN_START_RANGE=(int, 4),
    FIN_END_RANGE=(int, 26),
)

environ.Env.read_env(ENV_DIR)

DATABASE_SQLITE_ENABLED = env.str("DATABASE_SQLITE_ENABLED")

IDAP_SQLITE = env.str("SOMANS_SQLITE")
IDAP_CLUSTER = env.str("IDAP_CLUSTER")
IDAP_SERVER = env.str("IDAP_SERVER")
IDAP_USER = env.str("IDAP_USER")
IDAP_PWD = env.str("IDAP_PWD")
IDAP_DB = env.str("IDAP_DB")
IDAP_DB_PORT = env.str("IDAP_DB_PORT")
IDAP_DB_DRIVER = env.str("IDAP_DB_DRIVER")
IDAP_TDS_VERSION = env.str("IDAP_TDS_VERSION")

RSS_DB = env.str("RSS_DB")
RSS_DRIVER = env.str("RSS_DRIVER")
RSS_ODBC_DRIVER = env.str("RSS_ODBC_DRIVER")
RSS_INSTANCE = env.str("RSS_PR")
RSS_LOGS = env.str("RSS_LOGS")
RSS_PASSWORD = env.str("RSS_PASSWORD")
RSS_PORT = env.str("RSS_PORT")
RSS_SERVER = env.str("RSS_SERVER_PR01")
RSS_TDS_VERSION = env.str("RSS_TDS_VERSION")
RSS_USERNAME = env.str("RSS_USERNAME")
RSS_SCHEMA = env.str("RSS_SCHEMA")
RSS_LOG_TBL = env.str("RSS_LOG_TBL")
RSVR_CLUSTER = env.str("RSVR_CLUSTER")


FIN_SERVICE_FILE = env.str("FIN_SERVICE_FILE")
FIN_START_RANGE = env("FIN_START_RANGE")
FIN_END_RANGE = env("FIN_END_RANGE")
FIN_SERVICE_NAME = env.str("FIN_SERVICE_NAME")
FIN_SERVICE_FILE_NODE1 = env.str("FIN_SERVICE_FILE_NODE1")
FIN_SERVICE_FILE_NODE2 = env.str("FIN_SERVICE_FILE_NODE2")
FIN_NODE1_DIR = env.str("FIN_NODE1_DIR")
FIN_NODE2_DIR = env.str("FIN_NODE2_DIR")
FIN_SQLITE_TABLE = env.str("FIN_SQLITE_TABLE")
FIN_SQLITE_DB = env.str("FIN_SQLITE_DB")
FIN_SERVICES = env.str("FIN_SERVICES")
FIN_SERVICES_LOGS = env.str("FIN_SERVICES_LOGS")
FIN_SERVICES_TAG = env.str("FIN_SERVICES_TAG")
FIN_TABLE_HIST = env.str("FIN_TABLE_HIST")

IDAP_POS_DT_DIR = env.str("IDAP_POS_DT_DIR")
IDAP_POS_OUTPUT_DIR = env.str("IDAP_POS_OUTPUT_DIR")
IDAP_POS_LOGS = env.str("IDAP_POS_LOGS")
IDAP_POS_TAG = env.str("IDAP_POS_TAG")
IDAP_POS_TBL = env.str("IDAP_POS_TBL")
IDAP_LOG_TBL = env.str("IDAP_LOG_TBL")
IDAP_LOGS_DIR = env.str("IDAP_LOGS_DIR")

SOMANS_NEW_APP_SVR = env.str("SOMANS_NEW_APP_SVR")
SOMANS_NEW_APP_WKS = env.str("SOMANS_NEW_APP_WKS")
SOMANS_LS_OF_SVRS = env.str("SOMANS_LS_OF_SVRS")
SOMANS_LS_OF_WKS = env.str("SOMANS_LS_OF_WKS")
SOMANS_HEADCOUNT = env.str("SOMANS_HEADCOUNT")
SOMANS_BENCHMARK_SVRS = env.str("SOMANS_BENCHMARK_SVRS")
SOMANS_BENCHMARK_WKS = env.str("SOMANS_BENCHMARK_WKS")
SOMANS_SFTWR_SVRS = env.str("SOMANS_SFTWR_SVRS")
SOMANS_SFTWR_WKS = env.str("SOMANS_SFTWR_WKS")
SOMANS_APPRV_SFTWR = env.str("SOMANS_APPRV_SFTWR")
SOMANS_GRP_SFTWR = env.str("SOMANS_GRP_SFTWR")
SOMANS_LS_OF_SVRS_HIST = env.str("SOMANS_LS_OF_SVRS_HIST")
SOMANS_LS_OF_WKS_HIST = env.str("SOMANS_LS_OF_WKS_HIST")
SOMANS_HEADCOUNT_HIST = env.str("SOMANS_HEADCOUNT_HIST")
SOMANS_BENCHMARK_SVRS_HIST = env.str("SOMANS_BENCHMARK_SVRS_HIST")
SOMANS_BENCHMARK_WKS_HIST = env.str("SOMANS_BENCHMARK_WKS_HIST")
SOMANS_SFTWR_SVRS_HIST = env.str("SOMANS_SFTWR_SVRS_HIST")
SOMANS_SFTWR_WKS_HIST = env.str("SOMANS_SFTWR_WKS_HIST")
SOMANS_GRP_SFTWR_HIST = env.str("SOMANS_GRP_SFTWR_HIST")
SOMANS_HEADCOUNT_DATA = env.str("SOMANS_HEADCOUNT_DATA")

connection_string_idap = f"DRIVER={IDAP_DB_DRIVER};SERVER={IDAP_CLUSTER},{IDAP_DB_PORT};DATABASE={IDAP_DB};ENCRYPT=yes;TrustServerCertificate=Yes;MultiSubnetFailover=Yes;UID={IDAP_USER};PWD={IDAP_PWD}"
connection_url_idap = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string_idap})
engine_idap = create_engine(connection_url_idap)

connection_string_rss = f"DRIVER={RSS_ODBC_DRIVER};SERVER={RSVR_CLUSTER};DATABASE={RSS_DB};ENCRYPT=yes;TrustServerCertificate=Yes;MultiSubnetFailover=Yes;UID={RSS_USERNAME};PWD={RSS_PASSWORD}"
connection_url_rss = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string_rss})
engine_rss = create_engine(connection_url_rss)