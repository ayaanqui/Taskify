from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response

# Simple JWT
from rest_framework_simplejwt.tokens import RefreshToken

from users.models import Profile
from users.api.serializers import UserSerializer, UserAuthSerializer, UserRegisterSerializer, UserPrivateSerializer
from users.api.auth.permissions import AnonymousPermissionOnly

class UserAuthAPIView(APIView):
    serializer_class = UserAuthSerializer
    permission_classes = [AnonymousPermissionOnly]

    def post(self, request, *args, **kwargs):
        data = request.data
        username = data.get('username', None)
        password = data.get('password', None)

        if username == "" and password == "":
            return Response("All fields are required", status=400)
        
        qs = User.objects.filter(
            Q(username=username)|
            Q(email=username)
        )

        if qs.count() == 1:
            qs = qs.first()
            if qs.check_password(password):
                user = authenticate(username=qs.username, password=password)
                # login(request, user)

                refresh = RefreshToken.for_user(user)
                response = {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user': UserPrivateSerializer(user).data
                }
                return Response(response, status=200)
        
        return Response({"detail": "Incorrect username/email or password"}, status=401)


class UserRegisterAPIView(APIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AnonymousPermissionOnly]

    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        fullname = data.get('fullname.fullname', None)
        username = data.get('username', None)
        email = data.get('email', None)
        password = data.get('password', None)

        if fullname == "" and username == "" and email == "" and password == "":
            return Response("All fields are required", status=400)
        
        # Get objects to check if username and email are already in use
        username_obj = User.objects.filter(username=username)
        email_obj = User.objects.filter(email=email)

        # Form validation
        if username_obj.exists() and email_obj.exists():
            return Response([
                {
                    "username": "A user with that username already exists."
                },
                {
                    "email": "A user with that email already exists."
                }
            ], status=400)
        elif username_obj.exists():
            return Response({"username": "A user with that username already exists."}, status=400)
        elif email_obj.exists():
            return Response({"email": "A user with that email already exists."}, status=400)
        
        # Create user
        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()

        # Create user profile
        user_profile = Profile(user=user, fullname=fullname)
        user_profile.save()

        return Response({
            "detail": "Account created. You can now login"
        }, status=201)
