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
    if request.user.is_authenticated():
        if request.user.users.user_type==1:
            return render(request,'index_student.html',{'user':request.user})
        elif request.user.users.user_type==2:
            return render(request,'index_teacher.html',{'user':request.user})
    state=''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if request.user.users.user_type==1:
                return render(request,'index_student.html',{'user':request.user})
            elif request.user.users.user_type==2:
                return render(request,'index_teacher.html',{'user':request.user})
        else:
            state = 'not_exist_or_password_error'
    content = {
        'state': state,
    }
    return render(request, 'index_login.html', content)

@login_required
def set_password(request):
    state=''
    user=request.user
    if not request.user.is_authenticated():
        state="please login first"

    if request.method == 'POST':
        password = request.POST.get('password', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        email=request.POST.get('email','')
        if user.check_password(password) and user.email==email:
            if not password1:
                state = 'empty'
            elif password2 != password1:
                state = 'repeat_error'
            else:
                user.set_password(password1)
                user.save()
                state = 'success'
        else:
            state = 'password_error'
    content = {
        'user': user,
        'state': state,
    }
    return render(request, 'set_password.html', content)

def forget_password(request):
    state=''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        if username!='':
            if User.objects.filter(username=username):
                password1 = request.POST.get('password1', '')
                password2 = request.POST.get('password2', '')
                email=request.POST.get('email','')
                user=User.objects.get(username=username)
                if user.email == email:
                    if password1==password2:
                        user.set_password(password1)
                        user.save()
                        state='succeed'
                    else:
                        state="password_not_the_same"
                else:
                    state='wrong_email'
            else:
                state="user_not_exist"
        else:
            state="null_user_name"

    content = {
        'state': state,
    }
    return render(request, 'password.html', content)

def sign_up(request):
    state=''
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('send_index'))

    if request.method == 'POST':
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        user_type = 1 if request.POST.get('user_type')=="student" else 2
        if password1 == '' or password2 == '':
            state = 'empty'
        elif password1 != password2:
            state = 'repeat_error'
        else:
            username = request.POST.get('username', '')
            if User.objects.filter(username=username):
                state = 'user_exist'
            else:
                new_user = User.objects.create_user(username=username, password=password1,
                                                    email=request.POST.get('email', ''))
                new_user.save()
                new_my_user = Users(user=new_user,user_type=user_type)
                new_my_user.save()
                state = 'success'
                return HttpResponseRedirect(reverse('send_index'))
    content = {
        'state': state,
    }

    return render(request,'signup.html',content)

@login_required
def log_out(request):
    auth.logout(request)
    return redirect('send_index')


def stu_get_form(request):
    return render(request,"index_student.html")
def tea_set_form(request):
    #without handle the form
    user=request.user.users
    form_without_get=OrderForm.objects.filter(stu_and_tea=user,order_case='0')
    form_on_the_way=OrderForm.objects.filter(stu_and_tea=user,order_case='1')
    form_finished=OrderForm.objects.filter(stu_and_tea=user,order_case='2')
    content={
        "user":user,
        "form_without_get":form_without_get,
        "form_on_the_way":form_on_the_way,
        "form_finished":form_finished,
    }
    return render(request,"teacher.html",content)


def stu_get_detail(request):
    #without handle the form
    user=request.user.users
    form_on_the_way=OrderForm.objects.get(stu_and_tea=user,order_case='1')
    form_finished=OrderForm.objects.filter(stu_and_tea=user,order_case='2')
    content={
        'user':user,
        'form_on_the_way':form_on_the_way,
        'form_finished':form_finished,
    }
    return render(request,"student.html",content)

def teacher_get_detail(request):
    return render(request,"teacher.html")
def email(request):
    state=''
    user=request.user
    if not request.user.is_authenticated():
        state="please login first"

    if request.method == 'POST':
        password = request.POST.get('password', '')
        email1 = request.POST.get('email1', '')
        email2 = request.POST.get('email2', '')
        if user.check_password(password):
            if user.email==email1:
                user.email=email2
                user.save()
                state = 'success'
                return HttpResponseRedirect(reverse('send_index'))
            else:
                state='email_error'
        else:
            state = 'password_error'
    content = {
        'user': user,
        'state': state,
    }
    return render(request,"email.html",content)
