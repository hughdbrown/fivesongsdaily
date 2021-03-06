# Django settings for the fivesongs project.
import os.path
import logging

DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_ROOT = os.path.dirname(__file__)

AKISMET_API_KEY = ''

LOGOUT_URL = '/accounts/login/'

DATABASE_ENGINE = 'sqlite3'	    # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'fivesongsdaily.db'	    # Or path to database file if using sqlite3.
DATABASE_USER = ''              # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

LOGGING_LEVEL   = (logging.DEBUG if DEBUG else logging.WARNING)
LOGGING_LOGPATH = os.path.join(PROJECT_ROOT, 'logs')
LOGGING_LOGFILE = os.path.join(LOGGING_LOGPATH, DATABASE_NAME+'.log')
LOGGING_FORMAT  = "%(asctime)s [%(levelname)s] %(message)s"
LOGGING_DATEFMT = "%m-%d %H:%M:%S"

logging.basicConfig(level=LOGGING_LEVEL, format=LOGGING_FORMAT,
                    datefmt=LOGGING_DATEFMT, filename=LOGGING_LOGFILE, filemode="a")

SERVE_MEDIA = True        # Have webserver serving python serve local media, too
