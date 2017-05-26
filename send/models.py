# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import datetime
import random

from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

class FormManager(models.Manager):
    def query_on_the_way(self):
        query=self.get_queryset().filter(order_case='1')
        return query
    def query_without_send(self):
        query=self.get_queryset().filter(order_case='0')
        return query
    def query_has_send(self):
        query=self.get_queryset().filter(order_case='2')
        return query
    def query_get_query(self,slow_or_fast):
        if slow_or_fast=='0':
            query=self.get_queryset().filter(slow_or_fast='0')
        if slow_or_fast=='1':
            query=self.get_queryset().filter(slow_or_fast='1')
        return query


@python_2_unicode_compatible
class Users(models.Model):
    user = models.OneToOneField(User)
    user_type= models.IntegerField(default=0)
    phone_number = models.CharField(max_length=20)
    nick_name=models.CharField(max_length=20)

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
    pass_question1=models.CharField(max_length=100,default='')
    pass_answer1=models.CharField(max_length=50,default='')
    pass_question2=models.CharField(max_length=100,default='')
    pass_answer2=models.CharField(max_length=50,default='')
    gender = models.CharField(max_length=2,choices=GENDER_CHOICES,default='')
    grade = models.CharField(max_length=5,choices = GRADE_CHOICES,default='')
    Institute = models.CharField(max_length=50,default='')
    major=models.CharField(max_length=50,default='')
    
    sum_volun_time = models.IntegerField(default=0)
    bad_record = models.IntegerField(default=0)

    SENDORGET = (
        ('send','send'),
        ('get','get'),
    )
    send_or_get = models.CharField(max_length=5,choices = SENDORGET)
    address = models.EmailField(max_length=256)
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
    users_using = models.ManyToManyField(Users)
    # get_people = models.ForeignKey(TeacherUser)

    get_address = models.CharField(max_length = 256)
    send_address = models.CharField(max_length = 256)

    get_teacher = models.CharField(max_length = 20)
    send_teacher = models.CharField(max_length = 20)

    get_teacher_phone = models.CharField(max_length = 20)
    send_teacher_phone = models.CharField(max_length = 20)

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
    objects=FormManager()
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
