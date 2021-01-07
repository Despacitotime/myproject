#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# @Time : 2021/1/4 16:49 
# @Author : Despacitotime 
# @File : urls.py.py
from django.urls import path
from demo1 import views

# 路由列表，且名字必须为 urlpatterns
urlpatterns = {
    # 不能以/开头
    path('home/', views.home, name='home'),
    path('hello/', views.hello, name='hello')
}