#!/usr/bin/env python
# coding: utf8
# author: channel
#
from django.urls import path,re_path
from cmdb import views

app_name = 'cmdb'
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('assets/', views.assets, name='assets'),
    path('addhost/', views.addhost, name='addhost'),
    re_path('detail/(?P<nid>\d+)/', views.detail, name='detail'),
    re_path('edit/(?P<nid>\d+)/', views.edit, name='edit'),
    re_path('delete/(?P<nid>\d+)/', views.delete, name='delete'),
]
