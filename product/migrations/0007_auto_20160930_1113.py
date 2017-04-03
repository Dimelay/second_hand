# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-30 03:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import product.models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20160929_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='in_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 30, 11, 13, 39, 676267), verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0440\u0438\u0432\u043e\u0437\u0430'),
        ),
        migrations.AlterField(
            model_name='product',
            name='out_date',
            field=models.DateTimeField(blank=True, default=None, editable=False, null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0440\u043e\u0434\u0430\u0436\u0438'),
        ),
        migrations.AlterField(
            model_name='product',
            name='photo',
            field=models.FileField(blank=True, default=None, upload_to='media', verbose_name='\u0424\u043e\u0442\u043e'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pid',
            field=models.CharField(default=product.models.gen_pid, editable=False, max_length=50, unique=True, verbose_name='\u0410\u0440\u0442\u0438\u043a\u0443\u043b'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sold',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]