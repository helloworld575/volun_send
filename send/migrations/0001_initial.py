# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-13 07:51
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
                ('contain', models.CharField(blank=True, max_length=256)),
                ('order_number', models.CharField(max_length=15)),
                ('volunteer_time', models.IntegerField(default=0)),
                ('latest_get_time', models.DateTimeField()),
                ('get_order_time', models.DateTimeField()),
                ('latest_send_time', models.DateTimeField()),
                ('actual_send_time', models.DateTimeField()),
                ('pub_time', models.DateTimeField(auto_now=True)),
                ('slow_or_fast', models.CharField(choices=[('0', 'slow'), ('1', 'fast')], max_length=5)),
                ('other_import', models.TextField()),
                ('order_case', models.CharField(choices=[('0', 'without_get'), ('1', 'on_the_way'), ('2', 'has_send')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.IntegerField(default=0)),
                ('phone_number', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('\u5973', 'Male'), ('\u7537', 'Female')], max_length=2)),
                ('grade', models.CharField(choices=[('16', '\u5927\u4e00'), ('15', '\u5927\u4e8c'), ('14', '\u5927\u4e09'), ('13', '\u5927\u56db'), ('\u7855\u58eb', '\u7855\u58eb'), ('\u535a\u58eb', '\u535a\u58eb')], max_length=5)),
                ('Institute', models.CharField(max_length=50)),
                ('sum_volun_time', models.IntegerField(default=0)),
                ('bad_record', models.IntegerField(default=0)),
                ('send_or_get', models.CharField(choices=[('send', 'send'), ('get', 'get')], max_length=5)),
                ('address', models.EmailField(max_length=256)),
                ('sum_order_num', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='orderform',
            name='users_using',
            field=models.ManyToManyField(to='send.Users'),
        ),
    ]
