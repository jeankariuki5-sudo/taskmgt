from django.shortcuts import render
from rest_framework import viewsets, generics

from task.models import Task, Assigned_person
from task.serializers import TaskSerializer,Assigned_personSerializer

# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class Assigned_personListCreativeView(generics.ListCreateAPIView):
    queryset = Assigned_person.objects.all()
    serializer_class = Assigned_personSerializer


class Assigned_personDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assigned_person.objects.all()
    serializer_class = Assigned_personSerializer