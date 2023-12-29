import os
from pathlib import Path
import environ
import sqlalchemy
from sqlalchemy.engine import URL
from sqlalchemy import create_engine

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_DIR = str(Path(os.path.join(BASE_DIR, ".env")))

env = environ.Env(
    DJANGO_DEBUG=(bool, False),
    DEBUG_TOOLBAR=(bool, False),
    DATABASE_SQLITE_ENABLED=(bool, False),
    FIN_START_RANGE=(int, 4),
    FIN_END_RANGE=(int, 26),
)

environ.Env.read_env(ENV_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DJANGO_DEBUG")

APP_NAME = env.str("DJANGO_APP_NAME")
SOMANS_SQLITE = env.str("SOMANS_SQLITE")
SOMANS_ADMIN = env.str("SOMANS_ADMIN")
SOMANS_OPERATOR = env.str("SOMANS_OPERATOR")
SOMANS_NEW_APP_SVR = env.str("SOMANS_NEW_APP_SVR")
SOMANS_NEW_APP_WKS = env.str("SOMANS_NEW_APP_WKS")
SOMANS_NEW_APP_WKS1 = env.str("SOMANS_NEW_APP_WKS1")
SOMANS_LS_OF_SVRS = env.str("SOMANS_LS_OF_SVRS")
SOMANS_LS_OF_WKS = env.str("SOMANS_LS_OF_WKS")
SOMANS_HEADCOUNT = env.str("SOMANS_HEADCOUNT")
SOMANS_BENCHMARK_SVRS = env.str("SOMANS_BENCHMARK_SVRS")
SOMANS_BENCHMARK_WKS = env.str("SOMANS_BENCHMARK_WKS")
SOMANS_SFTWR_SVRS = env.str("SOMANS_SFTWR_SVRS")
SOMANS_SFTWR_WKS = env.str("SOMANS_SFTWR_WKS")
SOMANS_APPRV_SFTWR = env.str("SOMANS_APPRV_SFTWR")
SOMANS_GRP_SFTWR = env.str("SOMANS_GRP_SFTWR")

FIN_SERVICE_FILE = env.str("FIN_SERVICE_FILE")
FIN_START_RANGE = env("FIN_START_RANGE")
FIN_END_RANGE = env("FIN_END_RANGE")
FIN_SERVICE_NAME = env.str("FIN_SERVICE_NAME")
FIN_SERVICE_FILE_NODE1 = env.str("FIN_SERVICE_FILE_NODE1")
FIN_SERVICE_FILE_NODE2 = env.str("FIN_SERVICE_FILE_NODE2")
FIN_SERVICES = env.str("FIN_SERVICES")

IDAP_POS_DT_DIR = env.str("IDAP_POS_DT_DIR")
IDAP_ADMIN = env.str("IDAP_ADMIN")
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

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'simple_history',
    'import_export',
    # 'defender',
    'idap_application.apps.AppConfig',
    'idap_dap.apps.AppConfig',
    'idap_finservices.apps.AppConfig',
    'idap_database.apps.AppConfig',
    'idap_logs.apps.AppConfig',
    'idap_pos.apps.AppConfig',
    'somans_auth.apps.AppConfig',
    'somans_dashboard.apps.AppConfig',
    'somans_software.apps.AppConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'defender.middleware.FailedLoginMiddleware',
]

ROOT_URLCONF = 'somans.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'somans.wsgi.application'

# connection_string_idap = f"DRIVER={IDAP_DB_DRIVER};SERVER={IDAP_CLUSTER},{IDAP_DB_PORT};DATABASE={IDAP_DB};ENCRYPT=yes;TrustServerCertificate=Yes;MultiSubnetFailover=Yes;UID={IDAP_USER};PWD={IDAP_PWD}"
# connection_url_idap = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string_idap})
# engine_idap = create_engine(connection_url_idap)
#
# connection_string_rss = f"DRIVER={RSS_ODBC_DRIVER};SERVER={RSVR_CLUSTER};DATABASE={RSS_DB};ENCRYPT=yes;TrustServerCertificate=Yes;MultiSubnetFailover=Yes;UID={RSS_USERNAME};PWD={RSS_PASSWORD}"
# connection_url_rss = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string_rss})
# engine_rss = create_engine(connection_url_rss)

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if env("DATABASE_SQLITE_ENABLED"):
    SOMANS_ENGINE = sqlalchemy.create_engine(SOMANS_SQLITE)
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }

else:
    SOMANS_ENGINE = engine_idap
    # DATABASES = {"default": env.db()}
    DATABASES = {
        'default': {
            'ENGINE': 'mssql',
            'NAME': env.str('IDAP_DB'),
            'USER': env.str('IDAP_USER'),
            'PASSWORD': env.str('IDAP_PWD'),
            'HOST': env.str('IDAP_DB_HOST'),
            'PORT': env.str('IDAP_DB_PORT'),
            'OPTIONS': {  # Here
                'driver': 'ODBC Driver 17 for SQL Server',
                "Encrypt": True,
                "TrustServerCertificate": True,
            },
        }
    }

# be secure and clear DATABASE_URL since it is no longer needed.
# DATABASE_URL = None

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = False
EMAIL_HOST = '10.144.27.11'
EMAIL_HOST_USER = 'fredrick.amani@stanbic.co.tz'
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 25

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

LOGIN_REDIRECT_URL = env.str("DJANGO_LOGIN_REDIRECT_URL")

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / "static"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
