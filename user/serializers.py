from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('ratings', 'comments', 'favorites', 'role', 'email', 'name', 'password', 'avatar')
