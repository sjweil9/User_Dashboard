# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-20 01:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='desc',
            field=models.TextField(default='No description added.'),
        ),
    ]
