# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-10-22 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tax_app', '0005_auto_20191022_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='due_amount',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
