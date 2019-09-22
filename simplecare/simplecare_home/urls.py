from django.urls import path
from . import views

urlpatterns = [
    path('', views.simplecare, name = 'SimpleCare'),
]
