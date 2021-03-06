# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 04:26
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0013_auto_20161003_1610'),
    ]

    operations = [
        migrations.CreateModel(
            name='sale_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='in_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 10, 4, 12, 26, 27, 500702), verbose_name='\u0414\u0430\u0442\u0430 \u043f\u0440\u0438\u0432\u043e\u0437\u0430'),
        ),
        migrations.AddField(
            model_name='sale_log',
            name='product_pid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AddField(
            model_name='sale_log',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
