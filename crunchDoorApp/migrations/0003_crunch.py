# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crunchDoorApp', '0002_crunchmemoized_locationmemoized_productmemoized'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crunch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('extra_id', models.IntegerField(default=0, max_length=50)),
                ('permalink', models.CharField(max_length=150)),
                ('founded', models.CharField(max_length=150, null=True)),
                ('employees', models.IntegerField(default=0, null=True)),
                ('funding', models.IntegerField(default=0, null=True)),
                ('symbol', models.CharField(max_length=200, null=True)),
                ('similarcompany1', models.IntegerField(default=-1, max_length=50)),
                ('similarcompany2', models.IntegerField(default=-1, max_length=50)),
                ('similarcompany3', models.IntegerField(default=-1, max_length=50)),
                ('crunch_id', models.ForeignKey(null=True, db_column=b'company_id', to='crunchDoorApp.Company', unique=True)),
            ],
        ),
    ]
