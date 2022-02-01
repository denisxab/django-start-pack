"""
Этот файл необходим для настройки многопоточного WSGI (gunicorn)
"""
import os
from django.contrib.staticfiles.handlers import StaticFilesHandler
from django.core.wsgi import get_wsgi_application
from conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

if settings.DEBUG:
    # Для получения статических файлов при запуске `gunicorn` в режиме отладки
    application = StaticFilesHandler(get_wsgi_application())
else:
    application = get_wsgi_application()
