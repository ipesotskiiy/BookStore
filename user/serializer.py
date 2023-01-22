from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from bookstore.settings import DEFAULT_PORT, DEFAULT_ADDR

from product.serializer import BookSerializer

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)
    favorites = BookSerializer(many=True, required=False)
    avatar = serializers.SerializerMethodField('get_avatar')

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'avatar',
            'name',
            'favorites',
        )

    def get_avatar(self, obj):
        photo_url = f'http://{DEFAULT_ADDR}:{DEFAULT_PORT}{obj.avatar.url}'
        return photo_url


class UploadAvatarSerializer(serializers.ModelSerializer):
    avatar = serializers.FileField()

    class Meta:
        model = User
        fields = (
            'avatar',
        )


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        required=True, write_only=True, validators=[validate_password]
    )
    password2 = serializers.CharField(
        required=True, write_only=True
    )

    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'password2'
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, attrs):
        if not UniqueValidator(attrs['email']):
            raise serializers.ValidationError(
                {
                    'email': 'This email is already taken'
                }
            )

        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {
                    'password': 'Passwords do not match'
                }
            )

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']

        )
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        data['token'] = data.pop('access')
        data['refreshToken'] = data.pop('refresh')

        data.update({'user': UserSerializer(self.user).data})
        return data


class TokenObtainPairResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class TokenRefreshResponseSerializer(serializers.Serializer):
    access = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class TokenVerifyResponseSerializer(serializers.Serializer):
    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()


class TokenBlacklistResponseSerializer(serializers.Serializer):
    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()
