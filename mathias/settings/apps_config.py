# Application definitions


DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PACKAGE_APPS = [
    'django_extensions',
]

ADDITIONAL_APPS = [
    'core',
    'beetle',
]

INSTALLED_APPS = DJANGO_APPS + PACKAGE_APPS + ADDITIONAL_APPS