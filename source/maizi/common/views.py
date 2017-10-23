#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2015/11/3
@author: yopoing
Common模块View业务处理。
"""

from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import logout,login,authenticate
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password

# 首页
def index(request):
    # 广告
    ad_list = Ad.objects.all()
    # 关键字推荐
    keywords_list = RecommendKeywords.objects.all()
    # 最新课程
    new_course_list = Course.objects.all().order_by('-date_publish')
    # 最多播放
    play_course_list = Course.objects.all().order_by('-click_count')
    # 最具人气
    hot_course_list = Course.objects.all().order_by('favorite_count')
    # 推荐阅读(官方活动)
    read_av_list = RecommendedReading.objects.filter(reading_type='AV')
    # 推荐阅读（开发者资讯）
    read_nw_list = RecommendedReading.objects.filter(reading_type='NW')
    # 推荐阅读（技术交流）
    read_dc_list = RecommendedReading.objects.filter(reading_type='DC')
    # 友情链接
    link_list = Links.objects.all()
    # 名师风采
    teachers_list = UserProfile.objects.filter(groups__name='老师')

    return render(request, "common/index.html", locals())

# 登录
def login_check(request):
    username = request.GET.get('username',None)
    password = request.GET.get('password',None)
    user = authenticate(username=username,password=password)
    if user is not None:
        login(request,user)
        return redirect(request.META['HTTP_REFERER'])
    else:
        return JsonResponse({'info':'None'},safe=False)

# 注销
def logout_user(request):
    logout(request)
    return redirect(request.META['HTTP_REFERER'])

# 注册
def register(request):
    user_email = request.GET.get('username', None)
    user_pass = request.GET.get('password', None)
    user = UserProfile.objects.filter(username=user_email).exists()
    # print user
    if user is True:
        return JsonResponse({'info': 'exist'}, safe=False)
    else:
        user_reg = UserProfile.objects.create_user(user_email, password=make_password(user_pass, None, 'pbkdf2_sha256'))
        user_reg.save()
        user_reg.backend = 'django.contrib.auth.backends.ModelBackend'  # 声名使用哪个后台验证模块去做登录验证
        login(request, user_reg)
        return JsonResponse({'info': 'ok'}, safe=False)

# 课程关键字搜索
def careercourse(request):
    info_text = request.GET.get('com_input',None)
    info_data = Keywords
    info = info_data.objects.get(name=info_text)
    careercourse = info.careercourse_set.all()
    careercourse_list = []
    for inf in careercourse:
        img = str(inf.image)
        careercourse_list.append({'info':inf.name,'img':img})
        return JsonResponse(careercourse_list,safe=False)

# 其他课程搜索
def small_course(request):
    info_text = request.GET.get('com_input', None)
    info_data = Keywords
    info = info_data.objects.get(name=info_text)
    course = info.course_set.all()
    course_list = []
    for inf in course:
        course_list.append({'info': inf.name})
        return JsonResponse(course_list, safe=False)