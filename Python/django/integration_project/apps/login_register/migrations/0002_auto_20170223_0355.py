# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 03:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_register', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='dob',
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=200),
        ),
    ]
