""" Apps for reporting app """
from django.apps import AppConfig


class ReportingConfig(AppConfig):
    """ Reporting config class """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reporting'
