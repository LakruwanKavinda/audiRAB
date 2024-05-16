"""
Module-level docstring for notes/urls.py.

This module defines URL patterns for the notes app.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('authentication.urls')),

    # path('api/chat/', include('chat_api.urls')),
]
