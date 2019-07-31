from django.urls import path, include

# JWT
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from users.api.auth.views import UserAuthAPIView, UserRegisterAPIView

app_name = 'auth'

urlpatterns = [
    path('', UserAuthAPIView.as_view(), name='login'),
    path('register/', UserRegisterAPIView.as_view(), name='register'),
    path('refresh/', refresh_jwt_token, name='refresh'),
]