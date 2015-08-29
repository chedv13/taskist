# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.TimeStampedModel')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            bases=('core.timestampedmodel',),
        ),
    ]
