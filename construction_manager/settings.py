"""
Django settings for construction_manager project.
Render Deployment Configuration by AI Assistant.
"""

from pathlib import Path
from datetime import timedelta 
import os # <--- დავამატეთ: გარემოცვის ცვლადებისთვის
import dj_database_url # <--- დავამატეთ: PostgreSQL-ის კონფიგურაციისთვის

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# =======================================================
# 1. DEVELOPMENT / PRODUCTION CONTROL
# =======================================================

# Production-ის დროს, ეს ცვლადი Render-ზე იქნება დაყენებული.
# თუ ეს ცვლადი არსებობს, ვმუშაობთ PRODUCTION-ზე, თუ არა - DEVELOPMENT-ზე.
IS_RENDER_DEPLOYMENT = 'RENDER' in os.environ

# SECRET_KEY - მუდმივად უნდა იქნას წაკითხული გარემოცვის ცვლადებიდან PRODUCTION-ში
SECRET_KEY = os.environ.get(
    'SECRET_KEY', 
    'django-insecure-r4vjc46i)4il9fh5*heud&t#%2p@h*=701cq=#kxa^czh!6a^a' # ლოკალური გასაღები
)

# SECURITY WARNING: don't run with debug turned on in production!
if IS_RENDER_DEPLOYMENT:
    DEBUG = False
else:
    DEBUG = True # ლოკალური მუშაობისთვის

# =======================================================
# 2. ALLOWED HOSTS (დომენის ნებართვები)
# =======================================================

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

if IS_RENDER_DEPLOYMENT:
    # Render-ის დომენების მიღება
    RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
    if RENDER_EXTERNAL_HOSTNAME:
        ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
    
    # ეს დაშვებულია მხოლოდ Render-ისთვის. 
    # თუ DEBUG=False, Django არ მიიღებს კავშირებს თუ ჰოსტი დაუდასტურებელია.
    
# --- INSTALLED APPS (უცვლელი) ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-party apps
    'rest_framework',
    'rest_framework_simplejwt',
    'django_filters',
    # Local apps
    'core', 
    'tasks', 
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

# --- Static files (Production Configuration) ---
# აუცილებელია Render-ისთვის, რომ სტატიკური ფაილები (CSS, JS) სწორად დაამუშაოს.

STATIC_URL = 'static/'

if IS_RENDER_DEPLOYMENT:
    # Production-ში Django აგროვებს სტატიკურ ფაილებს ამ დირექტორიაში
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    
    # უსაფრთხოების დაჩქარება: HTTPS გადამისამართება
    SECURE_SSL_REDIRECT = True
    
    # პროქსიდან უსაფრთხო კავშირების მიღება
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


ROOT_URLCONF = 'construction_manager.urls'

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

WSGI_APPLICATION = 'construction_manager.wsgi.application'


# =======================================================
# 3. DATABASE CONFIGURATION (SQLite vs. PostgreSQL)
# =======================================================

if IS_RENDER_DEPLOYMENT:
    # PRODUCTION: გამოიყენება Render-ის DATABASE_URL ცვლადი PostgreSQL-ისთვის
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600,
        )
    }
else:
    # DEVELOPMENT: ლოკალურად იყენებს SQLite-ს
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# --- Password validation (უცვლელი) ---
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


# --- Internationalization (უცვლელი) ---
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# =======================================================
# 4. CUSTOM & API SETTINGS (უცვლელი)
# =======================================================

# Custom User Model-ის განსაზღვრა
AUTH_USER_MODEL = 'core.User' 

# REST Framework Settings (JWT-ს გამოყენებით)
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

# Simple JWT Settings
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "AUTH_HEADER_TYPES": ("Bearer",),
}