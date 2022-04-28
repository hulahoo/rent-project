import os

from configurations import Configuration
from environ import Env


class BaseConfiguration(Configuration):

    env = Env()
    Env.read_env('.env')

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    SECRET_KEY = env("SECRET_KEY")

    DEBUG = env("DEBUG")

    ALLOWED_HOSTS = ["*"]

    LOCAL_APPS = [
        "rent_app"
    ]

    THIRD_PARTY_APPS = [
        "rest_framework"
    ]

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ] + LOCAL_APPS + THIRD_PARTY_APPS

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'rental.urls'

    REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.AllowAny'
        ]
    }

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
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

    WSGI_APPLICATION = 'rental.wsgi.application'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': env("POSTGRES_DB"),
            'USER': env("POSTGRES_USER"),
            'PASSWORD': env("POSTGRES_PASSWORD"),
            'HOST': env("POSTGRES_HOST"),
            'PORT': env("POSTGRES_PORT")
        }
    }

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

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_TZ = True

    STATIC_URL = 'static/'

    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
