# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-02 09:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20211202_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 2, 12, 29, 10, 777280), verbose_name='Опубликована'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2021, 12, 2, 12, 29, 10, 777280), verbose_name='Дата'),
        ),
    ]
