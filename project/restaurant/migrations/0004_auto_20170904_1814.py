# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-09-04 18:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_auto_20170904_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_sent',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 4, 18, 14, 7, 161109), verbose_name='wysłano:'),
        ),
    ]
