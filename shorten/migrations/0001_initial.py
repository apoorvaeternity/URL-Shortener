# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-11 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('short', models.CharField(max_length=10)),
            ],
        ),
    ]