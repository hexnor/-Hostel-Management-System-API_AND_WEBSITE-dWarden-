# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 00:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usernamesave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('randomid', models.CharField(max_length=2, unique=True)),
                ('username', models.CharField(max_length=32)),
            ],
        ),
    ]
