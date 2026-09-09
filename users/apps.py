from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
    # Изменяет отображаемое имя блока в админке
    verbose_name = 'Authentication and Authorization'
