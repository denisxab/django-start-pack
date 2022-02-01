"""
Глобальные настройки `Django` проекта
"""
import os
import sys
from pathlib import Path
from pprint import pformat

from loguru import logger

sys.path.insert(0, "/".join(sys.path[0].split('/')[:-1]))
from helpful import read_env_file_and_set_from_venv, isDev, getEnv

# Полный путь к Django приложению
BASE_DIR = Path(__file__).resolve().parent.parent
# Полный путь к проекту
ROOT_DIR = "/".join(str(BASE_DIR).split('/')[:-1])
# Прочитать данными из файла с переменными окружениями
read_env_file_and_set_from_venv(os.path.join(ROOT_DIR, "__env.env"))
# Если `True` будет отображать отладочную информацию
DEBUG = isDev()
# Список хостов который будет обслуживать Django
ALLOWED_HOSTS = ['*']
# Секретный ключ для шифрования сессий
SECRET_KEY = getEnv("DJANGO_SECRET_KEY")
# Путь к wsgi файлу
WSGI_APPLICATION = 'conf.wsgi.application'
# Главный `URL` обработчик
ROOT_URLCONF = 'conf.urls'
#####


# Все инсталлированные приложения на вашем сайте.
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # React
    'frontend_react.apps.FrontendReactConfig',
]
# Список используемых плагинов.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
#####

# Список, содержащий настройки для всех шаблонизаторов, которые будут использоваться с Джанго.
# Каждый элемент списка представляет собой словарь, содержащий параметры для индивидуального двигатель.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Используемый шаблонный сервер.
        'DIRS': [],  # Каталоги, в которых движок должен искать исходные файлы шаблонов, в поиске порядок.
        'APP_DIRS': True,  # Должен ли движок искать исходные файлы шаблонов внутри установленного Приложения.
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
#####


# Словарь, содержащий настройки для всех баз данных, которые будут использоваться с Джанго.
DATABASES = {
    ## PostgreSQL
    # 'default': {
    #
    #        'ENGINE'  : 'django.db.backends.postgresql_psycopg2',  # Адаптер
    #        'NAME'    : os.environ.get('POSTGRES_DB', default=''),  # Имя Бд
    #        'USER'    : os.environ.get('POSTGRES_USER', default=''),  # Имя пользователя
    #        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', default=''),  # Пароль от пользователя
    #        'HOST'    : os.environ.get('POSTGRES_HOST', default='localhost'),  # Хост, имя контейнера.
    #        'PORT'    : os.environ.get('POSTGRES_PORT', default=5432),  # Порт для подключения к БД.
    # },

    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Автоматически добавлять поле primary_key к БД
#####


# Кеширование данных в файловой системе
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, '__cache')
    }
}
#####


# Список валидаторов, которые используются для проверки надежности паролей пользователей.
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
#####


# Логирование
logger.add(
    os.path.join(ROOT_DIR, 'deploy/log_django/all.log'),
    format="{time:YYYY-MM-DD-HH:mm:ss}‡{message}‡{file}‡{function}‡{level}‡{line}‡{exception}‡",
    level='INFO',
    rotation='100 KB',
    compression='zip',
)
logger.add(
    os.path.join(ROOT_DIR, 'deploy/log_django/error.log'),
    format="{time:YYYY-MM-DD-HH:mm:ss}‡{message}‡{file}‡{function}‡{level}‡{line}‡{exception}‡",
    level='ERROR',
    rotation='100 KB',
    compression='zip',
)
logger.add(
    os.path.join(ROOT_DIR, 'deploy/log_django/trace.log'),
    format="{time:YYYY-MM-DD-HH:mm:ss}‡{message}‡{file}‡{function}‡{level}‡{line}‡{exception}‡",
    level='SUCCESS',
    rotation='100 KB',
    compression='zip',
)
#####


# Локализация
LANGUAGE_CODE = 'ru'  # Язык сервера
USE_I18N = True  # Логическое значение, указывающее, должна ли быть включена система перевода Django.
TIME_ZONE = 'Europe/Moscow'  # Часовой пояс
USE_L10N = True  # Логическое значение, указывающее, будет ли включено локализованное форматирование данны
USE_TZ = True  # Логическое значение, указывающее, будут ли даты по умолчанию учитывать часовой пояс
#####


# Пути для статических файлы
STATIC_URL = '/static/'  # URL-адрес для использования при обращении к статическим файлам, расположенным в STATIC_ROOT.
STATIC_ROOT = os.path.join(BASE_DIR, "static/")  # Путь к общей статической папки.
STATICFILES_DIRS = [  # Список нестандартных путей используемых для сборки.
    # os.path.join(BASE_DIR, "static"),
]
# Пути для изображений
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Имя папки в корневом каталоге, для изображений
MEDIA_URL = '/media/'  # Добавляет к файлам префикс
#####


# Для отладки
if DEBUG:
    # django-debug-toolbar
    INSTALLED_APPS.append('debug_toolbar')
    INTERNAL_IPS = ['127.0.0.1']
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
    # Отключить кеширование при отладке
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        }
    }
#####


# Сохранить настройки запуска программы
logger.success(pformat({
    "BASE_DIR": BASE_DIR,
    "ROOT_DIR": ROOT_DIR,
    "DEBUG": DEBUG,
    "ALLOWED_HOSTS": ALLOWED_HOSTS,
    "SECRET_KEY": hash(SECRET_KEY),
    "WSGI_APPLICATION": WSGI_APPLICATION,
    "ROOT_URLCONF": ROOT_URLCONF,
    "INSTALLED_APPS": INSTALLED_APPS,
    "MIDDLEWARE": MIDDLEWARE,
    "DATABASES": DATABASES,
    "CACHES": CACHES,
    "LANGUAGE_CODE": LANGUAGE_CODE,
    "TIME_ZONE": TIME_ZONE,
    "STATIC_URL": STATIC_URL,
    "STATIC_ROOT": STATIC_ROOT,
    "STATICFILES_DIRS": STATICFILES_DIRS,
    "MEDIA_ROOT": MEDIA_ROOT,
    "MEDIA_URL": MEDIA_URL, }
))
#####
