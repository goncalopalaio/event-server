"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import dj_database_url
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'zf*$6af6y!-0!9gv9^f=*5x^_z#r0kz^@-=mw$clnuar#yxy7p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', 'events-rep.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'reporting.apps.ReportingConfig',
    'django.contrib.gis',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

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

WSGI_APPLICATION = 'project.wsgi.application'

# Configure Django App for Heroku.
django_heroku.settings(locals())

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

if os.getenv('DYNO'):
    DATABASE_CONFIG = dj_database_url.config()
else:
    local_database_path = "postgres://{}:{}@localhost:5432/event_reporting_db".format(os.environ["DJANGO_EVENT_USER"], os.environ["DJANGO_EVENT_PW"])
    DATABASE_CONFIG = dj_database_url.config(default=local_database_path)

DATABASES = {
    'default': DATABASE_CONFIG
}

DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

if os.getenv('DYNO'):
    GEOS_LIBRARY_PATH = "{}/libgeos_c.so".format(os.environ.get('GEOS_LIBRARY_PATH'))
    GDAL_LIBRARY_PATH = "{}/libgdal.so".format(os.environ.get('GDAL_LIBRARY_PATH'))
    PROJ4_LIBRARY_PATH = "{}/libproj.so".format(os.environ.get('PROJ4_LIBRARY_PATH'))
else:
    GDAL_LIBRARY_PATH = os.getenv('GDAL_LIBRARY_PATH')
    GEOS_LIBRARY_PATH = os.getenv('GEOS_LIBRARY_PATH')


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'