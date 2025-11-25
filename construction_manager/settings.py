import os
from pathlib import Path
import dj_database_url
from django.core.exceptions import ImproperlyConfigured

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# =======================================================================
# 1. ENVIRONMENT & SECURITY
# =======================================================================

# ლოკალური ტესტირებისთვის, თუ RENDER_EXTERNAL_HOSTNAME არ არის
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')

# DEBUG: ლოკალურად არის True, Production-ზე (Render-ზე) False
# Render-ზე ვიყენებთ გარემოცვის ცვლადს DJANGO_DEBUG
DEBUG = 'DJANGO_DEBUG' not in os.environ and 'DEBUG' in os.environ

# SECRET_KEY: აუცილებელია Production-ისთვის!
SECRET_KEY = os.environ.get(
    "SECRET_KEY", 
    "django-insecure-default-key-for-local-development-must-be-changed-in-production"
)

# ALLOWED_HOSTS: Production-ზე გვჭირდება Render-ის მისამართი
ALLOWED_HOSTS = []
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# =======================================================================
# 2. APPLICATION DEFINITION
# =======================================================================

INSTALLED_APPS = [
    # Django Apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third Party Apps
    'rest_framework',
    'django_filters',
    'rest_framework_simplejwt',
    
    # Your Apps
    'core',
    'tasks', # დავუშვათ, რომ თქვენი აპლიკაცია tasks-ია
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    
    # WhiteNoise Middleware for serving static files
    'whitenoise.middleware.WhiteNoiseMiddleware',
    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'construction_manager.urls'

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

WSGI_APPLICATION = 'construction_manager.wsgi.application'


# =======================================================================
# 3. DATABASE (Production/Development)
# =======================================================================

# PostgreSQL-ის კონფიგურაცია Render-ისთვის (Production)
if os.environ.get('DATABASE_URL'):
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600
        )
    }
# SQLite კონფიგურაცია (Local Development)
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }


# =======================================================================
# 4. AUTH & VALIDATION
# =======================================================================

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


# =======================================================================
# 5. INTERNATIONALIZATION
# =======================================================================

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# =======================================================================
# 6. STATIC FILES (CSS, JS, Images) - CRITICAL FOR ADMIN UI
# =======================================================================

# Base URL for static assets (e.g. /static/)
STATIC_URL = 'static/'

# Directory where Django will collect static files in Production
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Extra directories where static files reside (e.g. global static assets)
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Configure static file storage to use WhiteNoise for compressed files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# =======================================================================
# 7. DEFAULT PRIMARY KEY FIELD TYPE
# =======================================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# =======================================================================
# 8. REST FRAMEWORK SETTINGS (Optional, but useful)
# =======================================================================

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}