# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-25 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256, verbose_name=b'Name')),
                ('last_name', models.CharField(blank=True, max_length=256, verbose_name=b'SurName')),
                ('middle_name', models.CharField(blank=True, default=b'', max_length=256, verbose_name=b'FathersName')),
                ('birthday', models.DateField(null=True, verbose_name=b'Birthday Date')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=b'', verbose_name=b'Photo')),
                ('ticket', models.CharField(max_length=256, verbose_name=b'Ticket')),
                ('notes', models.TextField(blank=True, verbose_name=b'More info')),
            ],
        ),
    ]
