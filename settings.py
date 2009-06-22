import os, logging, sys

# Django settings for the fivesongs project.
try:
    from local_settings import *
except ImportError:
    try:
        from mod_python import apache
        apache.log_error( "local_settings.py not set; using default settings", apache.APLOG_NOTICE )
    except ImportError:
        import sys
        sys.stderr.write( "local_settings.py not set; using default settings\n" )

ADMINS = (
    ('', ''),
)
ADMIN_EMAIL = ''
MANAGERS = ADMINS
DEFAULT_FROM_EMAIL = ''

EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''

TIME_ZONE = 'America/Los Angeles'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = False

import django
DJANGO_ROOT = django.__path__[0]

MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'site_media/')
MEDIA_URL = '/site_media/'
ADMIN_MEDIA_PREFIX = '/media/'

SECRET_KEY = ''

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'middleware.project_logging.LoggingMiddleware',
)

ROOT_URLCONF = 'fivesongsdaily.urls'

TEMPLATE_ROOT = ''

TEMPLATE_DIRS = (
    #'/fivesongs/templates/',
    os.path.join(PROJECT_ROOT, 'templates/'),
    os.path.join(DJANGO_ROOT, 'contrib/admin/templates/')
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.comments',
    
    'fivesongsdaily.playlist',
    'fivesongsdaily.profiles',
    'fivesongsdaily.pages',
    'fivesongsdaily.contact',
    'fivesongsdaily.message',
)


