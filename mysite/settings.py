import os
import dj_database_url
from pathlib import Path

# Проекттин негизги папкасы
BASE_DIR = Path(__file__).resolve().parent.parent

# Коопсуздук жөндөөлөрү
SECRET_KEY = 'django-insecure-2z*&rg!%vl03^jh=ns6-y1k$u)=$3rgdx%fmh#a2%wjhr)z7j4'

# DEBUG: Render'де False болушу керек
DEBUG = True

ALLOWED_HOSTS = ['*']

# CSRF үчүн ишенимдүү шилтемелер
CSRF_TRUSTED_ORIGINS = [
    'https://travel-kg-5.onrender.com',
    'https://travel-project-9.onrender.com'
]

# Тиркемелер
INSTALLED_APPS = [
    'cloudinary_storage',         # Сөзсүз staticfiles'тан жогору турушу керек
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'cloudinary',
    'main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'travel_kg.urls' # travel_kg сиздин проекттин аты

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'travel_kg.wsgi.application'

# БАЗА ДАННЫХ (PostgreSQL кошулду)
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://travel_db_9vwk_user:BaH6Vi0JpIypu4Zl6TtSys8CFq1tt5sm@dpg-d6qor3v5gffc73ettia0-a.frankfurt-postgres.render.com/travel_db_9vwk',
        conn_max_age=600
    )
}

# Тил жөндөөлөрү
LANGUAGE_CODE = 'ky'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

LANGUAGES = [
    ('ky', 'Kyrgyz'),
    ('ru', 'Russian'),
    ('en', 'English'),
]

# Статикалык файлдар
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Медиа файлдар (Cloudinary)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dtuyalp6m',
    'API_KEY': '636667862685854',
    'API_SECRET': 'PgRp9Z7dBhdkoVTk0K1sa1I1390',
}

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# WhiteNoise статика жөндөөсү
if not DEBUG:
    STORAGES = {
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        },
    }

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'