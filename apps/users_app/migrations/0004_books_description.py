# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-18 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_app', '0003_authors_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]