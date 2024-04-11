# myproject/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='chat_englsih_index'),
    path('handle_message/', views.chat_with_ai, name='handle_message'),
    path('chat_with_ai/', views.chat_with_ai, name='chat_with_ai'),
]
