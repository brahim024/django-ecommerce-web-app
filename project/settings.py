"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""
import django_heroku
import os

# Braintree settings
#from django.core.exceptions import ImproperlyConfigured
#Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BRAINTREE_MERCHANT_ID = 'b3bnnwxfsghrr6vx' # Merchant ID
BRAINTREE_PUBLIC_KEY = '8bxwd7rxvjdxyjmg' # Public Key
BRAINTREE_PRIVATE_KEY = '7fda99ff4060aeb3b4a1618d92bb716a' # Private key
import braintree
BRAINTREE_CONF = braintree.Configuration(
 braintree.Environment.Sandbox,
 BRAINTREE_MERCHANT_ID,
 BRAINTREE_PUBLIC_KEY,
 BRAINTREE_PRIVATE_KEY
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '895Ee3Bb0F96Bb05Efb56E7D5C46D4E92898D5B65734A385'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['hexa-store.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'cart',
    'ecomapp',
    'order',
    'payment',
    'rest_framework',
    'bootstrap4',
    'ckeditor',
    'django_filters',
    #'django_celery_results',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR , 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/
CART_SESSION_ID='cart'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
     
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
django_heroku.settings(locals())
# here we added ckeditor

CKEDITOR_UPLOAD_PATH = "uploads/"
CKEDITOR_CONFIGS = {
    'awesome_ckeditor': {
        'toolbar': 'Basic',
        'toolbar': 'full',
        'height': 200,
        'width': 1002,
    },
}