"""rating config file"""
from django.apps import AppConfig


class RatingsConfig(AppConfig):
    """rating config class"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ratings'
