import base64

from django.core.files.base import ContentFile
from django.db import IntegrityError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.mixins import UpdateModelMixin
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView, TokenBlacklistView
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.core.files.uploadedfile import InMemoryUploadedFile

from user.models import User
from user.serializer import (
    UserSerializer,
    UserSerializer1,
    RegisterSerializer,
    MyTokenObtainPairSerializer,
    UploadAvatarSerializer,
    TokenObtainPairResponseSerializer,
    TokenRefreshResponseSerializer,
    TokenVerifyResponseSerializer, TokenBlacklistResponseSerializer
)


class RegisterUserAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                token = AccessToken.for_user(user)
                refreshToken = RefreshToken.for_user(user)
                resp = Response({"user": UserSerializer1(user, context=self.get_serializer_context()).data,
                                 "token": str(token), "refreshToken": str(refreshToken)
                                 })
                return resp

            else:
                return Response({"message": 'not valid'})

        except IntegrityError as e:
            account = User.objects.get(username='')
            account.delete()
            raise ValidationError({"400": f'{str(e)}'})

        except KeyError as e:
            print(e)
            raise ValidationError({"400": f'Field {str(e)} missing'})


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class GetProfileView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        try:
            http_token = request.META['HTTP_AUTHORIZATION']
            [bearer, token_value] = http_token.split(' ')
            token = AccessToken(token=token_value)
            token = token.payload
            user_id = token.get('user_id', None)
            user = User.objects.get(id=user_id)

            resp = Response({
                "user": UserSerializer(user).data,
            })
            return resp

        except Exception as e:
            raise ValidationError({"400": f'{str(e)}'})


class UpdateUserView(generics.UpdateAPIView, UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def patch(self, request, pk, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class UploadAvatarView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    parser_classes = [JSONParser]
    queryset = User.objects.all()
    serializer_class = UploadAvatarSerializer

    def patch(self, request, *args, **kwargs):
        try:
            formatb, imgstr = request.data['img'].split(';base64,')
            ext = formatb.split('/')[-1]

            data = ContentFile(base64.b64decode(imgstr), name=ext)

            base_path = InMemoryUploadedFile(data, field_name=None, name="myfile.jpg", content_type='image/jpeg',
                                             size=data.size, charset=None)
            request.user.avatar = base_path
            request.user.save()

            return Response({
                'ok': 'da'
            })

        except Exception as e:
            raise Exception(str(e))


class DecoratedTokenObtainPairView(TokenObtainPairView):
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenObtainPairResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class DecoratedTokenRefreshView(TokenRefreshView):
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenRefreshResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class DecoratedTokenVerifyView(TokenVerifyView):
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenVerifyResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class DecoratedTokenBlacklistView(TokenBlacklistView):
    @swagger_auto_schema(
        responses={
            status.HTTP_200_OK: TokenBlacklistResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
