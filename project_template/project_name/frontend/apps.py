from django.apps import AppConfig


class FrontendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'frontend'
    verbose_name = "Frontend React" # Красивое имя приложения в админ панели
