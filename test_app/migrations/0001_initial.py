# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-25 00:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_field', models.CharField(max_length=100, verbose_name='Test Field')),
            ],
        ),
    ]
