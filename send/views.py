# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

from .models import Users,OrderForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import user_passes_test,login_required
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import EmptyPage,Paginator,PageNotAnInteger
from django.core.urlresolvers import reverse
from .utils import teacher_check,student_check

def index(request):
    if request.user.is_authenticated()==False:
        return render(request,'index.html')
    if request.user.get_profile().user_type==1:
        return render(request,'student.html',{'user':request.user})
    elif request.user.get_profile().user_typej==2:
        return render(request,'teacher.html',{'user':request.user})

def signup(request):
    pass

def login(request):
    pass

@login_required
def logout(request):
    auth.logout(request)
    return redirect('index.html')

def setpassword(request):
    pass

@user_passes_test(teacher_check)
def add_send(request):
    pass

@user_passes_test(teacher_check)
def request_details(request):
    pass

@user_passes_test(student_check)
def request_send(request):
    pass

@user_passes_test(student_check)
def response_details(request):
    pass
