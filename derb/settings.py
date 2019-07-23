"""
Django settings for derb project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
from __future__ import absolute_import
import os
from django.core.urlresolvers import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cfx+9spw*3*rqf8*0vl2x+$b$vbz&!72p18!s0u!ivkd8jroz#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'report_builder',
    'presentation',
    'password_reset',
    'async_notifications',
    'ckeditor',
    "bootstrapform",
    'datetimewidget',
    'demo'

]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.locale.LocaleMiddleware',

]

ROOT_URLCONF = 'derb.urls'

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

WSGI_APPLICATION = 'derb.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'derb',
        'USER': 'derb',
        'PASSWORD': 'r3p0rt',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

AUTH_USER_MODEL = 'auth.User'

# django.contrib.auth
LOGIN_REDIRECT_URL = reverse_lazy('report_builder:index')
LOGIN_URL = reverse_lazy('auth_login')

# django-registration
ACCOUNT_ACTIVATION_DAYS = 7

DEFAULT_FROM_EMAIL = "mail@example.com"
EMAIL_HOST = "localhost"
EMAIL_PORT = "1025"

CELERY_MODULE = "derb.celery"
CELERY_TIMEZONE = TIME_ZONE
CELERY_ACCEPT_CONTENT = ['pickle', 'json']

from celery.schedules import crontab

CELERYBEAT_SCHEDULE = {
    # execute 12:30 pm
    'send_daily_emails': {
        'task': 'async_notifications.tasks.send_daily',
        'schedule': crontab(minute=30, hour=0),
    },
}

# CKEDITOR CONFIGS
DJANGO_WYSIWYG_FLAVOR = "ckeditor"

CKEDITOR_UPLOAD_PATH = "media/"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
        'height': 300,
        'width': '100%',
    },
    'basic': {
        'width': '100%',
        'toolbar': 'Basic',
        "toolbar_Basic": [['Source', '-', 'Save', 'NewPage', 'DocProps', 'Preview', 'Print', '-', 'Templates'],
                          ['Cut', 'Copy', 'Paste', 'PasteText',
                              'PasteFromWord', '-', 'Undo', 'Redo'],
                          ['Find', 'Replace', '-', 'SelectAll',
                              '-', 'SpellChecker', 'Scayt'],
                          ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
                           'HiddenField'],
                          ['Bold', 'Italic', 'Underline', 'Strike',
                              'Subscript', 'Superscript', '-', 'RemoveFormat'],
                          ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv',
                           '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr',
                           'BidiRtl'],
                          ['Link', 'Unlink', 'Anchor'],
                          ['Table', 'HorizontalRule', 'Smiley',
                              'SpecialChar', 'PageBreak'],
                          ['Styles', 'Format', 'Font', 'FontSize'],
                          ['TextColor', 'BGColor'],
                          ['Maximize', 'ShowBlocks', '-', 'About']],
        "language": "en",
        "skin": "moono",
    },
    'empty': {
        'toolbar': 'Basic',
        'height': 200,
        'width': 500,
        "toolbar_Basic": [],
        "language": "en",
        "skin": "moono",
    }
}

#DATE_INPUT_FORMATS = ('%d-%m-%Y')
INTERNAL_IPS = ['127.0.0.1']
