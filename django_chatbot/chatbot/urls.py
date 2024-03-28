from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.chatbot, name='chatbot'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('handle_message/', views.chatbot, name='handle_message'),
]
