# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-31 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_populate_words_tweets_redo_after_stemming'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='frequency',
            field=models.IntegerField(default=-1),
            preserve_default=False,
        ),
    ]