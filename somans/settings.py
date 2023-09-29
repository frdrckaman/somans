import os
from pathlib import Path
import environ
import sqlalchemy

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
SOMANS_ENGINE = sqlalchemy.create_engine(SOMANS_SQLITE)
SOMANS_ADMIN = env.str("SOMANS_ADMIN")
SOMANS_OPERATOR = env.str("SOMANS_OPERATOR")
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

FIN_SERVICE_FILE = env.str("FIN_SERVICE_FILE")
FIN_START_RANGE = env("FIN_START_RANGE")
FIN_END_RANGE = env("FIN_END_RANGE")
FIN_SERVICE_NAME = env.str("FIN_SERVICE_NAME")
FIN_SERVICE_FILE_NODE1 = env.str("FIN_SERVICE_FILE_NODE1")
FIN_SERVICE_FILE_NODE2 = env.str("FIN_SERVICE_FILE_NODE2")
FIN_SERVICES = env.str("FIN_SERVICES")

IDAP_POS_DT_DIR = env.str("IDAP_POS_DT_DIR")

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

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if env("DATABASE_SQLITE_ENABLED"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }

else:
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
