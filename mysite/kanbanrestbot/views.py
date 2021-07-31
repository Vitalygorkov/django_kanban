# https://www.youtube.com/watch?v=fGXqTnWAFOo

from django.shortcuts import render
from rest_framework import serializers
from rest_framework.views import APIVIew
from rest_framework.response import Response

from . import models
import random

# Create your views here.

class TaskSerializator(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = ['task_name', 'task_text']

class RandomTask(APIView):
    def get(self, *args, **kwargs):
        all_tasks = models.Task.objects.all()
        random_task = random.choice(all_tasks)
        serialized_random_task = TaskSerializator(random_task, many=False)
        return Response(serialized_random_task.data)