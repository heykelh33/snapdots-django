"""
Django settings for snapdots project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v7n0ykb+&+furgr(g)titmeaz(z4@ezm9m_-sifz2$o%kam+#1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = [u'172.16.1.54',u'192.168.42.1']    # son los ip de las interfaces de red del RPi
ALLOWED_HOSTS = [u'*']  #en produccion comentar esto y descomentar el de arriba por seguridad

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',                 #This is an administration site
    'django.contrib.auth',                  #This is an authentication framework
    'django.contrib.contenttypes',          #This is a framework for content types
    'django.contrib.sessions',              #This is a session framework
    'django.contrib.messages',              #This is a messaging framework
    'django.contrib.staticfiles',           #This is a framework for managing static files
    # 'sensors',                              #sensors App
    'channels',                             #channels App
    'worker',                         #sensorWorker App
    'radix'
]

# MIDDLEWARE_CLASSES is a tuple containing middlewares to be executed
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
#ROOT_URLCONF indicates the Python module where the root URL patterns of your application are defined
ROOT_URLCONF = 'snapdots.urls'
ROOT_PATH = os.path.abspath(os.path.dirname(__file__))
PROJECT_PATH = ROOT_PATH
PROJECT_NAME = os.path.basename(ROOT_PATH)
PROJECT_TEMPLATE_DIR = os.path.join(ROOT_PATH, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
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

WSGI_APPLICATION = 'snapdots.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES is a dictionary containing the settings for all the databases to be
# used in the project. There must always be a default database. The default
# configuration uses a SQLite3 database.

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'sensordb',
        'User':'cyberguille',
        'PASSWORD':'',
    }
}

#Base de datos mysql que hay que crear con usuario:snapdotsuser y passwd:snapdots
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'snapdots',
#         'USER': 'snapdotsuser',
#         'PASSWORD': 'snapdots',
#         'HOST': 'localhost',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

#LANGUAGE_CODE Defines the default language code for this Django site.
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

# channel layer asgi_redis
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "hosts":[('localhost',6379)],
        },
        "ROUTING": "snapdots.routing.channel_routing",
    },
}

# channel layer de asgiref.inmemory
# CHANNEL_LAYERS = {
#     "default": {
#         "BACKEND": "asgiref.inmemory.ChannelLayer",
#         "ROUTING": "snapdots.routing.channel_routing",
#     },
# }



