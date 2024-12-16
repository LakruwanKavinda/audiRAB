"""
URL configuration for authentication app.
"""

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    # Change 'login' to 'user_login'
    path('login/', views.login, name='login'),
    path('upload_pdf/', views.upload_pdf, name='upload_pdf'),
    path('search_pdf/', views.search_pdf, name='search_pdf'),
    path('generate_story/', views.generate_story, name='generate_story'),
    path('view_pdf/<int:pdf_id>/', views.view_pdf, name='view_pdf'),
    # chat
    path('send_message/', views.send_message, name='send_message'),
    path('get_messages/', views.get_messages, name='get_messages'),
]

