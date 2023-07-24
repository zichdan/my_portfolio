"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from django.core.management.utils import get_random_secret_key
from django.contrib.messages import constants as messages
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# setings for using dj_database_url and django_environ to setup your database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

import dj_database_url
# import environ

# env = environ.Env()

# environ.Env.read_env()



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ.get('SECRET_KEY')
SECRET_KEY = os.getenv('SECRET_KEY', get_random_secret_key)


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = os.environ.get('DEBUG', 'False').lower() == "true"
DEBUG = os.getenv('DEBUG', 'True')== "True"

# ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split()
# ALLOWED_HOSTS = []
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS','localhost').split(',')



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio',
    'authapp',
    'myproject',
    'bootstrap_datepicker_plus',  # Add the 'bootstrap_datepicker_plus' app to the list
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
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
        'DIRS': ['templates'],
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


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
# postgres://my_portfolio_g1uw_user:QZVldylu6MpLFtg6Ph7kwab6fghuPD6I@dpg-ciq49penqql4qa3olr70-a.oregon-postgres.render.com/my_portfolio_g1uw

DATABASE_URL = os.getenv('DATABASE_URL', None)
 
if not DATABASE_URL:    
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': os.getenv('DB_PORT'),
            'OPTIONS': {'sslmode': 'require'},
        }
    }
    


# # render postgresql database setup
# database_url = os.environ.get('DATABASE_URL')

# DATABASES['default'] = dj_database_url.parse(database_url)

    
    






# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}



#            CONTACT FORM EMAIL VAERIFICATION SETTINGS
# Configure the email backend to use SMTP
# Replace 'smtp.example.com' and '587' with your SMTP server and port.
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587

# Replace 'your_email@example.com' and 'your_email_password' with your email credentials.
EMAIL_HOST_USER = 'ezichdan@gmail.com'

EMAIL_HOST_PASSWORD = 'iwbzktpfpmngxfuc'

# Use TLS (Transport Layer Security) for secure connection with the SMTP server.
EMAIL_USE_TLS = True

# Set the email address that will be used as the 'From' address in sent emails.
# DEFAULT_FROM_EMAIL = 'your_email@example.com'

