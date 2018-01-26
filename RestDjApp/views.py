from django.shortcuts import render
from  rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task
class TaskView(viewsets.ModelViewSet):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
class CompletedTaskView(viewsets.ModelViewSet):
    queryset=Task.objects.all().filter(completed=True)
    serializer_class=TaskSerializer
class UnCompletedTaskView(viewsets.ModelViewSet):
    queryset=Task.objects.all().filter(completed=False)
    serializer_class=TaskSerializer
# Create your views here.
