from django.shortcuts import render

from rest_framework import viewsets
from .models import *
from .serializers import *


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    
    

