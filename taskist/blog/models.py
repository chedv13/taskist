__author__ = 'chedv13'

from django.db import models
from taskist.core.models import TimeStampedModel
from taskist.users.models import User
from django.contrib import admin


class Post(TimeStampedModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/images/%Y/%m/%d', blank=True, null=True)
    user = models.ForeignKey(User)

    class Meta:
        ordering = ['-created']


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'user_id', 'image')


admin.site.register(Post, PostAdmin)
