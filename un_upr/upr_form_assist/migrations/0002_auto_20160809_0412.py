# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-09 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upr_form_assist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upr_submission',
            name='authors',
            field=models.CharField(max_length=101),
        ),
    ]