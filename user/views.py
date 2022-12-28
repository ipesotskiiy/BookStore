from django.db import IntegrityError
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenViewBase
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken

from user.models import User
from user.serializer import UserSerializer, RegisterSerializer, MyTokenObtainPairSerializer


# Create your views here.
class RegisterUserAPIView(generics.CreateAPIView):
    # permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                print('valid')
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
                print('not valid')
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


class GetProfileView(TokenViewBase):
    # serializer_class = MyTokenObtainPairSerializer
    def get(self, request):
        try:

            # AccessToken(token=f"{request.META['HTTP_AUTHORIZATION']}".split(' ')[1]).payload.get('user_id', None)
                # user = serializer.save()
            request_token = AccessToken(token=f"{request.META['HTTP_AUTHORIZATION']}".split(' ')[1])
            resp = Response({
                 "user": UserSerializer({}, context=self.get_serializer_context()).data,
                 # "token": str(token),
                 "message": 'access is allowed'
            })
            return resp


        except Exception as e:
            raise ValidationError({"400": f'Field {str(e)} error'})
