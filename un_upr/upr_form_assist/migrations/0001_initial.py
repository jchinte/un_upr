# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-09 02:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('un_name', models.CharField(blank=True, max_length=100)),
                ('acronym', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UPR_question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('answer', models.TextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='UPR_submission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('authors', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UPR_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('streetAddress', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('website', models.URLField(blank=True)),
                ('Organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upr_form_assist.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='UserMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='upr_user',
            name='meta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='upr_form_assist.UserMeta'),
        ),
        migrations.AddField(
            model_name='upr_user',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='upr_question',
            name='submission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upr_form_assist.UPR_submission'),
        ),
        migrations.AddField(
            model_name='organization',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upr_form_assist.OrganizationTypes'),
        ),
        migrations.CreateModel(
            name='SampleQuestion',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('upr_form_assist.upr_question',),
        ),
    ]
