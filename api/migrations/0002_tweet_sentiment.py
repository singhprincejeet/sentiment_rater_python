# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-15 01:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_populate_sentiments'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='sentiment',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='api.Sentiment'),
            preserve_default=False,
        ),
    ]