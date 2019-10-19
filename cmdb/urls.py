#!/usr/bin/env python
# coding: utf8
# author: channel
#
from django.urls import path
from cmdb import views

app_name = 'cmdb'
urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('detail/', views.detail, name='detail'),
]
