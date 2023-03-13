import os
import environ


env = environ.Env(
    DEBUG=(bool, False)  # set casting, default value
)

environ.Env.read_env(env.str('ENV_PATH', '.env'))
DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')
DATABASES = {'default': env.db('DB_URL')}
ALLOWED_HOSTS = env('ALLOWED_HOSTS')

INSTALLED_APPS = ['datacenter']

ROOT_URLCONF = 'project.urls'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
