from django.urls import path, include

# Simple JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.api.auth.views import UserAuthAPIView, UserRegisterAPIView

app_name = 'auth'

urlpatterns = [
    path('', UserAuthAPIView.as_view(), name='login'),
    path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
]