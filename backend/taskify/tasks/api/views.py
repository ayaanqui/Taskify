from django.db.models import Q

from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from tasks.api.serializers import (
    TaskCreateSerializer,
    TaskDetailSerializer,
    TaskListSerializer
)
from tasks.models import Task
from users.api.auth.permissions import IsOwnerOrReadOnly, IsOwner


class TaskListAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = TaskListSerializer

    def get_queryset(self):
        qs = Task.objects.filter(user=self.request.user)
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(
                Q(task__icontains=query)|
                Q(detail__icontains=query)
            )
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskDetailAPIView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = TaskDetailSerializer
    lookup_field = 'id'
    queryset = Task.objects.all()

    def get(self, request, *args, **kwargs):
        completed = self.request.GET.get('completed', None)
        if completed and completed == 'true' or completed == 'false':
            if completed == 'true':
                completed_val = True
            else:
                completed_val = False
            
            task = Task.objects.get(id=kwargs.get('id', None), user=self.request.user)
            task.completed = completed_val
            task.save()
            
            return Response({'completed': completed}, status=200)
        else:
            return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)