from rest_framework import serializers

from tasks.models import Task
from users.api.serializers import UserSerializer


class TaskListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            'id',
            'task',
            'detail',
            'completed',
            'user',
            'due'
        ]
        read_only_fields = ['id', 'completed', 'user']
    
    def get_user(self, obj):
        return UserSerializer(obj.user).data


class TaskDetailSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            'id',
            'task',
            'detail',
            'completed',
            'user',
            'created',
            'due'
        ]
    
    def get_user(self, obj):
        return UserSerializer(obj.user).data


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            'task',
            'detail',
            'due'
        ]