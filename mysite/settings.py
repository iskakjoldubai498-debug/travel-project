import os
from pathlib import Path

try:
    import dj_database_url
except ImportError:
    dj_database_url = None
# Проекттин негизги папкасы
BASE_DIR = Path(__file__).resolve().parent.parent

# Коопсуздук жөндөөлөрү
SECRET_KEY = 'django-insecure-2z*&rg!%vl03^jh=ns6-y1k$u)=$3rgdx%fmh#a2%wjhr)z7j4'

# DEBUG: Серверде False болушу керек, бирок азырынча каталарды көрүү үчүн True калтырдык
DEBUG = True

ALLOWED_HOSTS = ['*']

# CSRF үчүн ишенимдүү шилтемелер (Render шилтемеңизди кошуңуз)
CSRF_TRUSTED_ORIGINS = [
    'https://travel-kg-5.onrender.com',
    'https://travel-project-9.onrender.com'
]

# Тиркемелер
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',  # Статика үчүн
    'django.contrib.staticfiles',
    'main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Статикалык файлдар үчүн
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # Тилдер (i18n) үчүн СӨЗСҮЗ керек
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite.urls'

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

WSGI_APPLICATION = 'mysite.wsgi.application'

# БАЗА ДАННЫХ (DATABASE)
# Render'де болсо PostgreSQL колдонот, локалдык болсо SQLite колдонот
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

if dj_database_url and os.environ.get('DATABASE_URL'):
    DATABASES['default'] = dj_database_url.config(conn_max_age=600)
# Тил жөндөөлөрү (Internationalization)
LANGUAGE_CODE = 'ky'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

LANGUAGES = [
    ('ky', 'Kyrgyz'),
    ('ru', 'Russian'),
    ('en', 'English'),
]

# Статикалык файлдар (CSS, JS, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Медиа файлдар (Жүктөлгөн сүрөттөр)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# WhiteNoise статикалык файлдарды серверде сактоо жөндөөсү
if not DEBUG:
    STORAGES = {
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        },
    }

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'