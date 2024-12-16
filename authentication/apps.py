
"""
Module for configuring the authentication app.
"""

from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """
    AppConfig class for the authentication app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'
