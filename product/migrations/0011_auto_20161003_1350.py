# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-03 05:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20161003_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='in_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 3, 13, 50, 19, 716879), verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0440\u0438\u0432\u043e\u0437\u0430'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.ImageField(upload_to='photo', verbose_name='\u0424\u043e\u0442\u043e'),
        ),
    ]
