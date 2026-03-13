import os
from pathlib import Path

# 1. Папкалардын жолу
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Коопсуздук жөндөөлөрү
SECRET_KEY = 'django-insecure-2z*&rg!%vl03^jh=ns6-y1k$u)=$3rgdx%fmh#a2%wjhr)z7j4'
DEBUG = True  # Сайт толук иштеп кеткенче True болуп турсун
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://travel-kg-5.onrender.com']

# 3. Колдонмолор (Apps)
INSTALLED_APPS = [
    'cloudinary_storage',          
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', 
    'cloudinary',                 
    'main',                       
]

# 4. Middleware
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

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'

# 5. База
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 6. Тил жана убакыт
LANGUAGE_CODE = 'ky'
LANGUAGES = [
    ('ky', 'Kyrgyz'),
    ('ru', 'Russian'),
    ('en', 'English'),
]
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 7. СТАТИКА ЖАНА МЕДИА (Django 6.0 шайкештиги)
STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'

# --- ЭҢ МААНИЛҮҮ БӨЛҮК (Катаны ушул чечет) ---
# Cloudinary китепканасы Django 6'дан таппай жаткан атрибуттарды кол менен коштук:
STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticCloudinaryStorage'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "cloudinary_storage.storage.StaticCloudinaryStorage",
    },
}

# Cloudinary API жөндөөсү
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'dffggv57z',
    'API_KEY': '159731443338952',
    'API_SECRET': 'CLOUDINARY_URL=cloudinary://<your_api_key>:<your_api_secret>@dffggv57z' # <--- URL ЭМЕС, КОДДУ ГАНА ЖАЗ!
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'