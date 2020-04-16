# Generated by Django 2.2.12 on 2020-04-16 22:36

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0031_auto_20200317_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='public_username',
            field=models.CharField(max_length=150, null=True, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')]),
        ),
    ]
