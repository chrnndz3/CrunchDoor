# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crunchDoorApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrunchMemoized',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('permalink', models.CharField(unique=True, max_length=150)),
                ('short_description', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='LocationMemoized',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('permalink', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=50, null=True)),
                ('street_1', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductMemoized',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('permalink', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
