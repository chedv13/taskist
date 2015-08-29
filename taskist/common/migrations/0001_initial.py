# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('timestampedmodel_ptr',
                 models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False,
                                      to='core.TimeStampedModel')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
            bases=('core.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('timestampedmodel_ptr',
                 models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False,
                                      to='core.TimeStampedModel')),
                ('object_id', models.PositiveIntegerField()),
                ('text', models.TextField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
            bases=('core.timestampedmodel',),
        ),
    ]
