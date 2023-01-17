from django.db import IntegrityError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.parsers import FileUploadParser, MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenViewBase, TokenRefreshView, \
    TokenBlacklistView
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.authentication import TokenAuthentication, get_authorization_header

from user.models import User
from user.serializer import (
    UserSerializer,
    RegisterSerializer,
    MyTokenObtainPairSerializer,
    UploadAvatarSerializer,
    TokenObtainPairResponseSerializer,
    TokenRefreshResponseSerializer,
    TokenVerifyResponseSerializer, TokenBlacklistResponseSerializer
)


# Create your views here.
class RegisterUserAPIView(generics.CreateAPIView):
    # permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                user = serializer.save()
                token = AccessToken.for_user(user)
                refreshToken = RefreshToken.for_user(user)
                # refreshToken.token_type = 'refreshToken'
                resp = Response({"user": UserSerializer(user, context=self.get_serializer_context()).data,
                                 # "message": "User Created Successfully.  Now perform Login to get your token",
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

    # serializer_class = MyTokenObtainPairSerializer
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
                # "token": token,
                # "message": 'access is allowed'
            })
            return resp

        except Exception as e:
            raise ValidationError({"400": f'{str(e)}'})


class UpdateUserView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def patch(self, request, pk, *args, **kwargs):
        queryset = User.objects.get(pk=self.kwargs['pk'])
        serializer = UserSerializer(queryset)
        if serializer.is_valid():
            serializer.save()
            return Response({'user': serializer.data})
        else:
            return Response({"message": 'not valid'})


# class UploadViewSet(ViewSet):
#     serializer_class = UploadAvatarSerializer
#
#     def list(self, request):
#         return Response("GET API")
#
#     def create(self, request):
#         avatar = request.FILES.get('avatar')
#         content_type = avatar.content_type
#         response = "POST API and you have uploaded a {} file".format(content_type)
#         return Response(response)

class UploadAvatarView(generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    parser_classes = [JSONParser]  # MultiPartParser ]
    queryset = User.objects.all()
    serializer_class = UploadAvatarSerializer

    def patch(self, request, *args, **kwargs):
        try:
            current_user = request.user
            serializer = self.get_serializer(data=UploadAvatarSerializer(current_user).data['avatar'])
            if serializer.is_valid(raise_exception=True):
                serializer.perform_update()

            return Response({
                'avatar': serializer.data
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
