from django.db import models
from taskist.core.models import TimeStampedModel
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from taskist.users.models import User


class Comment(TimeStampedModel):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    user = models.ForeignKey(User)

    class Meta:
        ordering = ['-created']


class Like(TimeStampedModel):
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    text = models.TextField()
    user = models.ForeignKey(User)

    class Meta:
        ordering = ['-created']
