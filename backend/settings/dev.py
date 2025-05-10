from .base_settings import *


INSTALLED_APPS += [
    'rest_framework',
    'corsheaders',
    'base.apps.BaseConfig'
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
] + MIDDLEWARE


CORS_ALLOW_ALL_ORIGINS = True

ALLOWED_HOSTS = ['*', 'backend']

MEDIA_URL = '/images/'

STATICFILES_DIRS = [
    BASE_DIR / 'static'
]

MEDIA_ROOT = 'static/images'

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "class": "logging.FileHandler",
            "filename": "general.log",
            "level": "DEBUG",
        }
    },
    "loggers": {
        "base": {
            "level": "DEBUG",
            "handlers": ["file"]
        }
    }
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'book_blog_db',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',
        'PORT': '5432',
    }
}