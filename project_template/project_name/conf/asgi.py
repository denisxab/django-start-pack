"""
Для асинхронной работы
"""

import os

from django.contrib.staticfiles.handlers import StaticFilesHandler
from django.core.asgi import get_asgi_application

from conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')

if settings.DEBUG:
    # Для получения статических файлов при запуске  в режиме отладки
    application = StaticFilesHandler(get_asgi_application())
else:
    application = get_asgi_application()
