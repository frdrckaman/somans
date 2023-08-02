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