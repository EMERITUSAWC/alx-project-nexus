# nexus_backend/settings.py

"""
Django settings for Nexus Backend project.
Fully configured for Render deployment with environment variables.
"""

import os
from pathlib import Path

# -------------------------
# BASE DIRECTORY
# -------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------
# SECRET KEY
# -------------------------
# IMPORTANT: For production, set this in Render's environment variables
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'replace-this-with-a-secret-key')

# -------------------------
# DEBUG
# -------------------------
# Turn off in production by setting DEBUG=False in Render environment
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# -------------------------
# ALLOWED HOSTS
# -------------------------
# Set this in Render environment, e.g., ALLOWED_HOSTS=yourapp.onrender.com
ALLOWED_HOSTS = [
    # Allowed hosts for Render deployment
    "abagna-alx-nexus-project-lw0z.onrender.com",  # Your Render URL
    "localhost",  # For local testing
    "127.0.0.1",  # For local testing

]

# -------------------------
# INSTALLED APPS
# -------------------------
INSTALLED_APPS = [
    # Default Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Your apps
    'nexusapp_accounts',
    'nexusapp_orders',
    'nexusapp_products',

    # Third-party apps
    'rest_framework',
    'rest_framework_simplejwt',
    'django_filters',
    'corsheaders',
    'django_extensions',
    'drf_yasg',
]

# -------------------------
# MIDDLEWARE
# -------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Handles CORS
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -------------------------
# ROOT URL CONF
# -------------------------
# This must match the root urls.py you created in the project root
ROOT_URLCONF = 'urls'

# -------------------------
# TEMPLATES
# -------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Look for templates in this folder
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

# -------------------------
# WSGI
# -------------------------
WSGI_APPLICATION = 'nexus_backend.wsgi.application'

# -------------------------
# DATABASE
# -------------------------
# Default: SQLite for simplicity, good for initial Render deployment
# For production, switch to PostgreSQL or MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -------------------------
# PASSWORD VALIDATION
# -------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -------------------------
# INTERNATIONALIZATION
# -------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Accra'
USE_I18N = True
USE_TZ = True

# -------------------------
# STATIC FILES
# -------------------------
STATIC_URL = '/static/'  # URL for accessing static files
STATIC_ROOT = BASE_DIR / 'staticfiles'  # Where collectstatic will put files
STATICFILES_DIRS = [
    BASE_DIR / "static",  # Your app static files
]

# -------------------------
# MEDIA FILES
# -------------------------
MEDIA_URL = '/media/'  # URL for media files
MEDIA_ROOT = BASE_DIR / 'media'  # Directory to store uploaded files

# -------------------------
# CORS (Cross-Origin Resource Sharing)
# -------------------------
CORS_ALLOW_ALL_ORIGINS = True  # Allow all origins (good for testing)
# For production, you can limit to your frontend URL

# -------------------------
# REST FRAMEWORK CONFIG (optional)
# -------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
}

# -------------------------
# DEFAULT AUTO FIELD
# -------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -------------------------
# SECURITY SETTINGS (optional)
# -------------------------
# Enable in production
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# -------------------------
# LOGGING (optional, useful for debugging on Render)
# -------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}
