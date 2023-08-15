import environ

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