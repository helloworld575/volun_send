# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import datetime
import random

from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone


@python_2_unicode_compatible
class StudentUser(models.Model):
    user = models.OneToOneField(User)

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

    gender = models.CharField(max_length=2,choices=GENDER_CHOICES)
    grade = models.CharField(max_length=5,choices = GRADE_CHOICES)
    Institute = models.CharField(max_length=50)
    sum_volun_time = models.IntegerField(default=0)
    bad_record = models.IntegerField(default=0)


    def __str__(self):
        return self.user.username

class TeacherUser(models.Model):
    SENDORGET = (
        ('send','send'),
        ('get','get'),
    )
    user=models.OneToOneField(User)
    send_or_get = models.CharField(max_length=5,choices = SENDORGET)
    address = models.EmailField(max_length=256)
    phone_number = models.CharField(max_length=20)
    sum_order_num = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class OrderForm(models.Model):
    first_order = -1

    SLOWORFAST = (
        ('0','slow'),
        ('1','fast'),
    )

    ORDERCASE = (
        ('0','without_get'),
        ('1','on_the_way'),
        ('2','has_send'),
    )
    teachers = models.ManyToManyField(TeacherUser)
    # get_people = models.ForeignKey(TeacherUser)
    send_student = models.ForeignKey(StudentUser)

    get_address = models.CharField(max_length = 256)
    send_address = models.CharField(max_length = 256)

    contain = models.CharField(max_length=256,blank=True)

    order_number=models.CharField(max_length=15)       #YYYYMMDDIIIIIRR

    volunteer_time = models.IntegerField(default =0)

    latest_get_time = models.DateTimeField()
    get_order_time = models.DateTimeField()
    latest_send_time = models.DateTimeField()
    actual_send_time = models.DateTimeField()
    pub_time = models.DateTimeField(auto_now=True)

    slow_or_fast = models.CharField(max_length=5,choices=SLOWORFAST)

    other_import = models.TextField()

    order_case = models.CharField(max_length=20,choices = ORDERCASE)     # 1-order without get 2-order on the way 2 order has sent
    # order_without_get = models.ForeignKey(TeacherUser)
    # order_on_the_way = models.ForeignKey(TeacherUser)
    # order_has_get = models.ForeignKey(TeacherUser)
    #
    # has_got_order = models.ForeignKey(StudentUser)
    # has_send_order = models.ForeignKey(StudentUser)

    def __str__(self):
        return self.order_number
    def get_first_order(self):
        if self.first_order < 0:
            self.first_order = OrderForm.objects.order_by('-order_number')[0].first_order+1
        else:
            self.first_order +=1

        return self.first_order

    @classmethod
    def gen_order_num(self):
        num = str(self.get_first_order())
        n = 5-len(num)
        return self.pub_time.year()+self.pub_time.month()+self.pub_time.day()+'0'*n+num+str(random(10,99))
