from django.urls import path

from user.views import RegisterUserAPIView, UserDetailAPI

app_name = 'user'

urlpatterns = [
    path('signin', UserDetailAPI.as_view(), name='signin'),
    path('signup', RegisterUserAPIView.as_view(), name='signup')
]

