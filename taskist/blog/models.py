__author__ = 'chedv13'

from django.db import models
from taskist.users.models import User
from django.contrib import admin


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/posts/images/%Y/%m/%d', blank=True, null=True)
    user = models.ForeignKey(User)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'user_id', 'image')


admin.site.register(Post, PostAdmin)
