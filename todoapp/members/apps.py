from django.apps import AppConfig


class MemebersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'memebers'

class NewAppConfig(AppConfig):
  name = 'members'