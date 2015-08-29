# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20150829_1328'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='text',
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default=b''),
        ),
    ]
