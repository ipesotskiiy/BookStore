from django.db import IntegrityError
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.views import TokenObtainPairView
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
                access = AccessToken.for_user(user)
                refresh = RefreshToken.for_user(user)
                resp = Response({"user": UserSerializer(user, context=self.get_serializer_context()).data,
                                 "message": "User Created Successfully.  Now perform Login to get your token",
                                 "access": str(access), "refresh": str(refresh)
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
