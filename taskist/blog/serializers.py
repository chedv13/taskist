__author__ = 'chedv13'

from rest_framework import serializers
from taskist.blog.models import Post
from taskist.users.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'user', 'image', 'content')
        depth = 1
