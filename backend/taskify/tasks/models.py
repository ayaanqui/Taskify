from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.utils import timezone


class Task(models.Model):
    task = models.CharField(max_length=300, blank=False, null=False)
    detail = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    priority = models.IntegerField(
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)
        ],
        blank=True,
        null=True
    )

    def __str__(self):
        return f'Task({self.task})'