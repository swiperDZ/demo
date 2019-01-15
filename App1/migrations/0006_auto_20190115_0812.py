# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-01-15 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0005_auto_20190115_0804'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='u_birth_day',
            field=models.IntegerField(max_length=4, null=True, verbose_name='出生日'),
        ),
        migrations.AddField(
            model_name='user',
            name='u_birth_month',
            field=models.IntegerField(max_length=8, null=True, verbose_name='出生月'),
        ),
        migrations.AlterField(
            model_name='user',
            name='u_birth_year',
            field=models.IntegerField(max_length=8, null=True, verbose_name='出生年'),
        ),
        migrations.AlterField(
            model_name='user',
            name='u_sex',
            field=models.CharField(choices=[('male', '男性'), ('female', '女性')], max_length=8, verbose_name='性别'),
        ),
    ]
