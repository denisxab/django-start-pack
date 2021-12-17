"""
Глобальные настройки `Django` проекта
"""
import os
import re
from pathlib import Path
from pprint import pprint

from loguru import logger

BASE_DIR = Path(__file__).resolve().parent.parent  # Полный путь к проекту
ROOT_DIR = "/".join(str(BASE_DIR).split('/')[:-1])


def read_env_file_and_set_from_venv(file_name: str):
	"""Чтение переменных окружения из указанного файла, и добавление их в ПО `python`"""
	with open(file_name, 'r', encoding='utf-8') as _file:
		res = {}
		for line in _file:
			tmp = re.sub(r'^#[\s\w\d\W\t]*|[\t\s]', '', line)
			if tmp:
				k, v = tmp.split('=', 1)
				# Если значение заключено в двойные кавычки, то нужно эти кавычки убрать
				if v.startswith('"') and v.endswith('"'):
					v = v[1:-1]
				
				res[k] = v
	os.environ.update(res)
	pprint(res)


read_env_file_and_set_from_venv(os.path.join(ROOT_DIR, "__env.env"))

DEBUG = True  # Если `True` будет отображать отладочную информацию
ALLOWED_HOSTS = ['*']  # Список хостов который будет обслуживать Django
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")  # Секретный ключ для шифрования сессий

WSGI_APPLICATION = 'conf.wsgi.application'

ROOT_URLCONF = 'conf.urls'  # Главный `URL` обработчик
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

# Список, содержащий настройки для всех шаблонизаторов, которые будут использоваться с Джанго. Каждый элемент списка представляет собой словарь, содержащий параметры для индивидуального двигатель.
TEMPLATES = [
		{
				'BACKEND' : 'django.template.backends.django.DjangoTemplates',  # Используемый шаблонный сервер.
				'DIRS'    : [],  # Каталоги, в которых движок должен искать исходные файлы шаблонов, в поиске порядок.
				'APP_DIRS': True,  # Должен ли движок искать исходные файлы шаблонов внутри установленного Приложения.
				'OPTIONS' : {
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
				'NAME'  : BASE_DIR / 'db.sqlite3',
		}
}
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # Автоматически добавлять поле primary_key к БД
#####


# Кеширование данных в файловой системе
CACHES = {
		'default': {
				'BACKEND' : 'django.core.cache.backends.filebased.FileBasedCache',
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
#####


#####


# Локализация
LANGUAGE_CODE = 'ru'  # Язык сервера
USE_I18N = True  # Логическое значение, указывающее, должна ли быть включена система перевода Django.
TIME_ZONE = 'Europe/Moscow'  # Часовой пояс
USE_L10N = True  # Логическое значение, указывающее, будет ли включено локализованное форматирование данны
USE_TZ = True  # Логическое значение, указывающее, будут ли даты по умолчанию учитывать часовой пояс
#####


# Пути для статические файлы
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
	
	## django-livereload-server
	# INSTALLED_APPS.append('livereload')
	# MIDDLEWARE.append('livereload.middleware.LiveReloadScript')
	
	# Отключить кеширование при отладке
	CACHES = {
			'default': {
					'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
			}
	}
#####
