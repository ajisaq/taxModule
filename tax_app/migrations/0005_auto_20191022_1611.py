# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-10-22 15:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tax_app', '0004_auto_20191021_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='bn_rc',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='business',
            name='owner_name',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='business',
            name='tax_collector',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]