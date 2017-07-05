"""
Django settings for reactive_eshop project.

Generated by 'django-admin startproject' using Django 1.11.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

from os.path import abspath, dirname, join


##########################
#   PATH CONFIGURATION   #
##########################
here = lambda *x: join(abspath(dirname(__file__)), *x)
PROJECT_ROOT = here("..")
root = lambda *x: join(abspath(PROJECT_ROOT), *x)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ck0*kq=+p%d=tzynzp@&^o!4bv&&5^68x(3wqmz7%$+e*aj5yj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'webpack_loader',
    'graphene_django',
    'product',
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

ROOT_URLCONF = 'reactive_eshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [root('templates')]
        ,
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

WSGI_APPLICATION = 'reactive_eshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': root('db.sqlite3'),
    }
}


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = root('static')
STATICFILES_DIRS = (
    # CSS files
    # ('css', root('static/css')),

    # Fonts
    # ('fonts', root('static/fonts')),

    # JS files
    ('js', root('static/js')),

    # Images
    # ('img/rs-img', root('static/img/rs-img')),
    # ('img/icons', root('static/img/icons')),
    # ('img/logo', root('static/img/logo')),
    # ('img/favicons', root('static/img/favicons')),
)


MEDIA_URL = '/media/'
MEDIA_ROOT = root('media')


WEBPACK_LOADER = {
    'DEFAULT': {
        # Must end with slash. Also, this must match ONLY the bundle dir name (without any parent dir names).
        # Just the bundle's dir name. If we changed it to "static/js/" then it would compiled to
        # <script src="localhost:8000/static/static/js/vendors.js"></script> which is wrong.
        'BUNDLE_DIR_NAME': 'js/',
        'STATS_FILE': root('static/js/webpack-stats.json'),
    }
}

# GRAPHENE = {
#     'SCHEMA': 'reactive_eshop.schema.schema'  # Where my Graphene schema lives
# }
