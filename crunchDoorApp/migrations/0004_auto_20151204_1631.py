# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crunchDoorApp', '0003_crunch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crunchmemoized',
            name='short_description',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
