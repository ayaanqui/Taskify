from django.urls import path

from tasks.api.views import TaskListAPIView, TaskDetailAPIView

app_name = 'tasks'

urlpatterns = [
    path('', TaskListAPIView.as_view(), name='list'),
    path('<int:id>/', TaskDetailAPIView.as_view(), name='detail')
]
