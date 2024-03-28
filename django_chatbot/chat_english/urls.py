# myproject/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='chat_englsih_index'),
    path('add_dialog/', views.add_dialog, name='add_dialog'),
    path('send_message/', views.send_message, name='send_message'),
    path('chat_with_ai/', views.chat_with_ai, name='chat_with_ai'),
]
