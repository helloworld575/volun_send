# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-29 08:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('get_address', models.CharField(max_length=256)),
                ('send_address', models.CharField(max_length=256)),
                ('get_teacher', models.CharField(max_length=20)),
                ('send_teacher', models.CharField(max_length=20)),
                ('get_teacher_phone', models.CharField(max_length=20)),
                ('send_teacher_phone', models.CharField(max_length=20)),
                ('get_student', models.CharField(max_length=20)),
                ('get_student_phone', models.CharField(max_length=20)),
                ('contain', models.CharField(blank=True, max_length=256)),
                ('order_number', models.CharField(default='', max_length=15)),
                ('volunteer_time', models.CharField(default='0', max_length=5)),
                ('latest_get_time', models.DateTimeField(null=True)),
                ('get_order_time', models.DateTimeField(null=True)),
                ('latest_send_time', models.DateTimeField(null=True)),
                ('actual_send_time', models.DateTimeField(null=True)),
                ('pub_time', models.DateTimeField(null=True)),
                ('slow_or_fast', models.CharField(max_length=5)),
                ('other_import', models.TextField(blank=True)),
                ('order_case', models.CharField(blank=True, max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.IntegerField(default=0)),
                ('phone_number', models.CharField(max_length=20)),
                ('nick_name', models.CharField(default='', max_length=20)),
                ('pass_question1', models.CharField(default='', max_length=100)),
                ('pass_answer1', models.CharField(default='', max_length=50)),
                ('pass_question2', models.CharField(default='', max_length=100)),
                ('pass_answer2', models.CharField(default='', max_length=50)),
                ('gender', models.CharField(default='', max_length=2)),
                ('grade', models.CharField(default='', max_length=5)),
                ('Institute', models.CharField(default='', max_length=50)),
                ('major', models.CharField(default='', max_length=50)),
                ('sum_volun_time', models.IntegerField(default=0)),
                ('bad_record', models.IntegerField(default=0)),
                ('sum_order_num', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='orderform',
            name='stu_and_tea',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='send.Users'),
        ),
    ]
