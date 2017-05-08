# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import datetime

from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

@python_2_unicode_compatible
class TeacherUser(AbstractUser):
    name= models.CharField('teacher_name',max_length=50)
    address = models.EmailField(max_length=256)
    phone_number = models.CharField('phone_number',max_length=20)
    sum_order_num = models.IntegerField()
    order_without_get = models.ForeignKey('OrderForm')
    order_on_the_way = models.ForeignKey('OrderFoem')
    order_has_get = models.ForeignKey('OrderForm')

    def __str__(self):
        return self.name
@python_2_unicode_compatible
class StudentUser(AbstractUser):

    GENDER_CHOICES = (
        ('女','Male'),
        ('男','Female'),
    )
    GRADE_CHOICES = (
        ('16','大一'),
        ('15','大二'),
        ('14','大三'),
        ('13','大四'),
        ('硕士','硕士'),
        ('博士', '博士'),
    )

    name = models.CharField('student_name',max_length=50)
    gender = models.CharField(max_length=2,choices=GENDER_CHOICES)
    grade = models.CharField(max_length=5,choices = GRADE_CHOICES)
    Institute = models.CharField(max_length=50)
    phone_number = models.CharField('phone_number',max_length=20)
    show_myself = models.TextField('introduction',default='')
    has_got_order = models.ForeignKey('OrderForm')
    has_send_orde = models.ForeignKey('OrderForm')
    sum_volun_time = models.IntegerField()
    bad_record = models.IntegerField()

    def __str__(self):
        return self.name


class OrderForm(models.Model):
    send_people = models.ForeignKey(TeacherUser)
    get_people = models.ForeignKey(TeacherUser)
    send_student = models.ForeignKey(StudentUser)
    get_address = models.CharField(max_length = 256)
    send_address = models.CharField(max_length = 256)
    contain = models.CharField(max_length=256,blank=True)
    order_number=models.ForeignKey('OrderNumber',blank=False)
    volunter_time = models.IntegerField()
    latest_get_time = models.DateTimeField()
    actual_get_time = models.DateTimeField()
    latest_send_time = models.DateTimeField()
    actual_send_time = models.DateTimeField()
    get_order_time = models.DateTimeField()
    pub_time = models.DateTimeField(auto_now=true)
    get_or_not = models.BooleanField(default = False)
    send_or_not = models.BooleanField(default = False)
    slow_or_fast = models.BooleanField(default = False)#slow in default
    other_import = models.TextField()

    def __str__(self):
        return self.order_number

class OrderNumber(models.MOdel):
    pass
