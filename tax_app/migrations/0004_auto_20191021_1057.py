# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-10-21 09:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tax_app', '0003_auto_20191020_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='category',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='tax_app.Business_Category'),
        ),
        migrations.AddField(
            model_name='business',
            name='due_amount',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='business',
            name='due_date',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='business',
            name='payment_status',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
