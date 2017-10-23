#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2015/11/3
@author: yopoing
common模块的url配置。
"""

from django.conf.urls import patterns, url
from common.views import index,login_check,logout_user,careercourse,small_course,register
import django
from django import views

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^ad/(?P<path>.*)$',django.views.static.serve, {'document_root': 'images/ad/'},name='ad'),
    url(r'^login_check/$', login_check, name='login_check'),
    url(r'^logout/$', logout_user, name='logout'),
    url(r'^careercourse',careercourse,name='careercourse'),
    url(r'^small_course',small_course,name='small_course'),
    url(r'^register', register, name='register'),
    url(r'^course/(?P<path>.*)$',django.views.static.serve, {'document_root': 'images/course/'},name='course'),
    url(r'^links/(?P<path>.*)$', django.views.static.serve, {'document_root': 'images/links/'}, name='links'),

]
