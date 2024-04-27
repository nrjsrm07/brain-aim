# settings.py

from pathlib import Path
import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')

MONGODB_USER = os.getenv('MONGODB_USER')
MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD')
MONGODB_HOST = os.getenv('MONGODB_HOST')
MONGODB_APP = os.getenv('MONGODB_APP')

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR =os.path.join(BASE_DIR, 'templates')
STATIC_DIR =os.path.join(BASE_DIR, 'static')


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r!=3ta=yu-6&5opwf1&yxlz+_z6gpyt7y=q0!%hmpcm@ytxc06'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Set CSRF_COOKIE_SECURE to False for development purposes
# CSRF_COOKIE_SECURE = False

# Optionally, set CSRF_COOKIE_HTTPONLY to True for added security
# CSRF_COOKIE_HTTPONLY = True

CSRF_TRUSTED_ORIGINS = [
    'https://brain-aim.onrender.com',
]

ALLOWED_HOSTS = ['brain-aim.onrender.com', "127.0.0.1"]

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gameapp',
    # 'corsheaders',
    'core',
    #Third party app
    'rest_framework',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    "https://brain-aim.onrender.com",
]
ROOT_URLCONF = 'TruthOrDare.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'TruthOrDare.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE':'django.db.backends.postgresql_psycopg2',
#         'NAME': POSTGRES_DB,
#         'USER': POSTGRES_USER,
#         'PASSWORD': POSTGRES_PASSWORD,
#         'HOST': POSTGRES_HOST,
#         'PORT': POSTGRES_PORT,
#         }
#     }

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'CLIENT': 
        {
            'host': f'mongodb+srv://{MONGODB_USER}:{MONGODB_PASSWORD}@{MONGODB_HOST}/?retryWrites=true&w=majority&appName={MONGODB_APP}',
        }
    }
}

# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS=[STATIC_DIR,]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Email Backend Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  
EMAIL_HOST = os.getenv('EMAIL_HOST')  
EMAIL_PORT = os.getenv('EMAIL_PORT')  
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')  
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')  
