# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from django.db import models
from django import forms
from .models import Users,OrderForm

# class StudentUserAdmin(admin.ModelAdmin):
#     list_display = ('')
admin.site.register(Users)
admin.site.register(OrderForm)
