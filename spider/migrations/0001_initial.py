# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-17 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bitrate', models.IntegerField()),
                ('genre', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('frequency', models.CharField(max_length=200)),
                ('adress', models.CharField(max_length=200)),
                ('telephone', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('site', models.CharField(max_length=200)),
            ],
        ),
    ]