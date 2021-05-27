from django.urls import path, include
from . import views
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views







urlpatterns = [
    path('', views.index, name='home'),
]