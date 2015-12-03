# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('website', models.CharField(default=b'0', max_length=100)),
                ('total_Reviews', models.IntegerField(default=0)),
                ('average', models.DecimalField(default=0, max_digits=3, decimal_places=2)),
                ('logo', models.CharField(default=b'0', max_length=200)),
                ('industry', models.CharField(default=b'0', max_length=50)),
            ],
        ),
    ]
