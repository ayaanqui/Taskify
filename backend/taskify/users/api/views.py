from django.db.models import Q
from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import permissions

from users.api.serializers import UserSerializer

class UserListAPIView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self, *args, **kwargs):
        q = self.request.GET.get('q', None)
        if q is not None:
            qs = User.objects.filter(
                Q(username__icontains=q)|
                Q(email__icontains=q)
            )
            return qs
        return User.objects.all()


class UserDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'