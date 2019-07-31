from django.urls import path, include

from users.api.views import UserListAPIView, UserDetailAPIView

app_name = 'users'

urlpatterns = [
    path('', UserListAPIView.as_view(), name='list'),
    path('<str:username>/', UserDetailAPIView.as_view(), name='detail')
]