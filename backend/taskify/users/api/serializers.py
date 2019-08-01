from django.contrib.auth.models import User

from rest_framework import serializers

from users.models import Profile
from users.api.profiles.serializers import UserProfileSerializer

class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'profile',
        ]
    
    def get_profile(self, obj):
        user = User.objects.get(id=obj.id)
        qs = Profile.objects.filter(user=user)
        return UserProfileSerializer(qs.first()).data


class UserPrivateSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'profile',
            'email'
        ]
    
    def get_profile(self, obj):
        user = User.objects.get(id=obj.id)
        qs = Profile.objects.filter(user=user)
        return UserProfileSerializer(qs.first()).data


class UserAuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]


class UserProfileFullnameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['fullname']


class UserRegisterSerializer(serializers.ModelSerializer):
    fullname = UserProfileFullnameSerializer(source='*')

    class Meta:
        model = User
        fields = [
            'fullname',
            'username',
            'email',
            'password'
        ]
        extra_kwargs = {
            'password': {
                'style': {
                    'input_type': 'password'
                },
                'write_only': True
            }
        }