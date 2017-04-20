# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 02:54
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0034_auto_20170406_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='in_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 6, 10, 54, 10, 281996), verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0440\u0438\u0432\u043e\u0437\u0430'),
        ),
        migrations.AlterField(
            model_name='product',
            name='out_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2017, 4, 6, 10, 54, 10, 282032), editable=False, null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0440\u043e\u0434\u0430\u0436\u0438'),
        ),
        migrations.AlterField(
            model_name='sale_log',
            name='action',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.action', verbose_name='\u0414\u0435\u0439\u0441\u0442\u0432\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='sale_log',
            name='dates',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 6, 10, 54, 10, 281126)),
        ),
    ]
