# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-15 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20180815_0015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=140)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('tweet', models.ManyToManyField(to='api.Tweet')),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
    ]