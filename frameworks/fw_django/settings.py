import pathlib


# == Directories == #

BASE_DIR = pathlib.Path(__file__).parent

ROOT_URLCONF = 'urls'


# == Common == #

SECRET_KEY = 'spq(1(5k%bd8xapm3o1i%zm33(ugf_nhnl*c*832jg&x5w4rfs'

DEBUG = True

ALLOWED_HOSTS = ['*']

WSGI_APPLICATION = 'wsgi.application'

# == Applications == #

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


# == Middleware== #

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

AUTH_PASSWORD_VALIDATORS = []


# == Static and Templates == #

STATIC_URL = '/static/'

STATIC_ROOT = (BASE_DIR / 'static').as_posix()

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


# == Databases == #

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': (BASE_DIR / 'db.sqlite3').as_posix(),
    }
}


# == Internationalization == #

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

