from django.urls import path
from rest_framework_simplejwt import views
from user.views import RegisterUserAPIView, MyTokenObtainPairView

app_name = 'user'

urlpatterns = [
    path('signup', RegisterUserAPIView.as_view(), name='signup'),
    # path('signin', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('signin', MyTokenObtainPairView.as_view(), name='signin'),
    path('check-token', views.TokenRefreshView.as_view(), name='token_refresh'),
]
