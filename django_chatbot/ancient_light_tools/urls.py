from django.urls import path
from . import views

urlpatterns = [
    path('sentence_split', views.sentence_split, name='sentence_split'),

]
