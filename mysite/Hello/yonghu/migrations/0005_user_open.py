# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-06 09:33
from __future__ import unicode_literals

from django.db import migrations, models
import yonghu.models


class Migration(migrations.Migration):

    dependencies = [
        ('yonghu', '0004_auto_20170906_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='open',
            field=models.TextField(default=yonghu.models.User.open_default),
        ),
    ]