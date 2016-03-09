# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-09 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public_IP', models.GenericIPAddressField(verbose_name='public IP')),
                ('private_IP', models.GenericIPAddressField(verbose_name='private IP')),
                ('pub_key', models.TextField(verbose_name='pub Key')),
            ],
        ),
    ]
