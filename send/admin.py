# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from django.db import models
from django import forms
from .models import StudentUser,TeacherUser,OrderForm

# class StudentUserAdmin(admin.ModelAdmin):
#     list_display = ('')
admin.site.register(StudentUser)
admin.site.register(TeacherUser)
admin.site.register(OrderForm)
