# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-22 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date_hired',
            field=models.DateField(),
        ),
    ]