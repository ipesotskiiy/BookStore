from django.urls import path
from rest_framework_simplejwt import views
from user.views import RegisterUserAPIView, MyTokenObtainPairView, GetProfileView

app_name = 'user'

urlpatterns = [
    path('auth/signup', RegisterUserAPIView.as_view(), name='signup'),
    path('auth/signin', MyTokenObtainPairView.as_view(), name='signin'),
    path('auth/check-token', views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/me', GetProfileView.as_view(), name='me')
    # path('user/me', views.TokenVerifyView.as_view(), name='me')

]
