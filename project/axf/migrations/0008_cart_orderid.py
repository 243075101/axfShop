# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-15 01:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0007_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='orderid',
            field=models.CharField(default='0', max_length=20),
        ),
    ]
