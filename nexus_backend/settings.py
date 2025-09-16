"""
Django settings for nexus_backend project.
ALX Project Nexus – Comprehensive configuration for development and production.
"""

import os
from pathlib import Path
from datetime import timedelta

# ------------------------------------------------------------------------------
# BASE DIRECTORY
# ------------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------------------------------------------------------------
# SECURITY SETTINGS
# ------------------------------------------------------------------------------
# ⚠️ Replace with your own unique secret key for production.
SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "replace-this-with-a-secure-random-string-for-production"
)

# Debug should be False in production!
DEBUG = os.environ.get("DJANGO_DEBUG", "True") == "True"

# Add your deployed domain(s) or server IP here for production.
# nexus_backend/settings.py

ALLOWED_HOSTS = [
    "127.0.0.1",    # Localhost IP
    "localhost",    # Localhost hostname
    "your-app.onrender.com",  # Your Render or production URL (replace with real URL)
]

# ------------------------------------------------------------------------------
# APPLICATION DEFINITION
# ------------------------------------------------------------------------------
INSTALLED_APPS = [
    # Django default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'rest_framework',           # Django REST Framework for APIs
    'corsheaders',              # Handle cross-origin requests

    # Local apps (replace with your actual app names)
    'nexusapp_accounts',
    'nexusapp_products',
    'nexusapp_orders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',          # Enable CORS
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nexus_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Add your global templates folder if needed
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'nexus_backend.wsgi.application'

# ------------------------------------------------------------------------------
# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# 💡 Use SQLite for development. Switch to PostgreSQL for production.
DATABASES = {
    'default': {
        'ENGINE': os.environ.get("DB_ENGINE", 'django.db.backends.sqlite3'),
        'NAME': os.environ.get("DB_NAME", BASE_DIR / 'db.sqlite3'),
        'USER': os.environ.get("DB_USER", ''),
        'PASSWORD': os.environ.get("DB_PASSWORD", ''),
        'HOST': os.environ.get("DB_HOST", ''),
        'PORT': os.environ.get("DB_PORT", ''),
    }
}

# ------------------------------------------------------------------------------
# PASSWORD VALIDATION
# ------------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ------------------------------------------------------------------------------
# INTERNATIONALIZATION
# ------------------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# ------------------------------------------------------------------------------
# STATIC & MEDIA FILES
# ------------------------------------------------------------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']   # Local static folder
STATIC_ROOT = BASE_DIR / 'staticfiles'     # Collected static for production

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ------------------------------------------------------------------------------
# DEFAULT PRIMARY KEY FIELD TYPE
# ------------------------------------------------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ------------------------------------------------------------------------------
# DJANGO REST FRAMEWORK SETTINGS
# ------------------------------------------------------------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

# ------------------------------------------------------------------------------
# CORS HEADERS SETTINGS
# ------------------------------------------------------------------------------
# Allow all origins for dev. Restrict this in production.
CORS_ALLOW_ALL_ORIGINS = True

# ------------------------------------------------------------------------------
# SECURITY HEADERS (Recommended for Production)
# ------------------------------------------------------------------------------
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# ------------------------------------------------------------------------------
# LOGGING (Optional but recommended)
# ------------------------------------------------------------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {'class': 'logging.StreamHandler'},
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}

# ------------------------------------------------------------------------------
# OPTIONAL: SIMPLE JWT CONFIG (If you add JWT auth later)
# ------------------------------------------------------------------------------
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('Bearer',),
}


