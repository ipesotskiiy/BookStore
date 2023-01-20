from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from product import serializer as SS

from product.serializer import BookSerializer

from user.models import User


# class Base64FileField(serializers.FileField):
#
#     def to_internal_value(self, data):
#         from django.core.files.base import ContentFile
#         import base64
#         import six
#         import uuid
#
#         if isinstance(data, six.string_types):
#             if 'data:' in data and ';base64,' in data:
#                 header, data = data.split(';base64,')
#
#             try:
#                 decoded_file = base64.b64decode(data)
#             except TypeError:
#                 self.fail('invalid_image')
#
#             file_name = str(uuid.uuid4())[:12]
#             file_extension = self.get_file_extension(file_name, decoded_file)
#
#             complete_file_name = "%s.%s" % (file_name, file_extension, )
#
#             data = ContentFile(decoded_file, name=complete_file_name)
#
#         return super(Base64FileField, self).to_internal_value(data)
#
#     def get_file_extension(self, file_name, decoded_file):
#         import imghdr
#         extension = imghdr.what(file_name, decoded_file)
#         extension = 'jpg' if extension == 'jpeg' or extension == 'png' else extension
#         return extension


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
        photo_url = 'http://localhost:8000'+obj.avatar.url
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
        # The default result (access/refresh tokens)
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        data['token'] = data.pop('access')
        data['refreshToken'] = data.pop('refresh')

        # Custom data you want to include
        data.update({'user': UserSerializer(self.user).data})
        # and everything else you want to send in the response
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
