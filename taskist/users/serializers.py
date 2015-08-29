__author__ = 'chedv13'

from rest_framework import serializers
from taskist.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'avatar')
