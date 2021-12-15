"""
Главный маршрутизатор `URL`
"""

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from conf import settings
from api.api_v1 import api as api_v1

urlpatterns = [
    path('admin/', admin.site.urls),
    # Маршрутизация `Api`
    path('api/v1/', api_v1.urls),
    # Маршрутизация `React`
    path('reat_test/', include('frontend.urls')),
    # path('', include('<main_app>.urls')),
]


# Для debug_toolbar и отдачи статических фалов / медиа фалов
if settings.DEBUG:
    # Для отладчика
    import debug_toolbar

    urlpatterns.append(
            path('__debug__/', include(debug_toolbar.urls)),
    )

    # Для работы static
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

    # Для работы  media
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
