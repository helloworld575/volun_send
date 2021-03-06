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
    nick_name=models.CharField(max_length=20,default='')

    pass_question1=models.CharField(max_length=100,default='')
    pass_answer1=models.CharField(max_length=50,default='')
    pass_question2=models.CharField(max_length=100,default='')
    pass_answer2=models.CharField(max_length=50,default='')

    gender = models.CharField(max_length=2,default='')
    grade = models.CharField(max_length=5,default='')
    Institute = models.CharField(max_length=50,default='')
    major=models.CharField(max_length=50,default='')

    sum_volun_time = models.IntegerField(default=0)
    bad_record = models.IntegerField(default=0)

    sum_order_num = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username


class OrderForm(models.Model):
    first_order = models.IntegerField(default=-1)

    stu_and_tea = models.ForeignKey(Users)       #the one who publish it
    # get_people = models.ForeignKey(TeacherUser)
    get_address_case=models.CharField(max_length=3)
    send_address_case=models.CharField(max_length=3)
    get_address = models.CharField(max_length = 256)

    send_address = models.CharField(max_length = 256)

    get_teacher = models.CharField(max_length = 20)
    send_teacher = models.CharField(max_length = 20)

    get_teacher_phone = models.CharField(max_length = 20)
    send_teacher_phone = models.CharField(max_length = 20)

    get_student=models.CharField(max_length=20)
    get_student_phone=models.CharField(max_length=20)

    contain = models.CharField(max_length=256,blank=True)

    order_number=models.CharField(max_length=15,default='')       #YYYYMMDDIIIII

    volunteer_time = models.CharField(max_length=5,default='0')

    '''time:
        1-10
        8:00-17:00'''
    latest_get_time = models.DateTimeField(null=True)
    get_order_time = models.DateTimeField(null=True)
    latest_send_time = models.DateTimeField(null=True)
    actual_send_time = models.DateTimeField(null=True)

    pub_time = models.DateTimeField(null=True)

    slow_or_fast = models.CharField(max_length=5)

    other_import = models.TextField(blank=True)

    order_case = models.CharField(max_length=2,blank=True)     # 1-order without get 2-order on the way 2 order has sent
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
        self.first_order = OrderForm.objects.order_by('-order_number')[0].first_order+1
        return self.first_order

    @classmethod
    def gen_order_num(cls,self):
        number = str(cls.get_first_order(self))
        n = 5-len(number)
        return str(self.pub_time.year)+str(self.pub_time.month)+str(self.pub_time.day)+'0'*n+number
