from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from rest_framework import viewsets, status
from .models import *
from .serializers import *


class TaskViewSet(viewsets.ModelViewSet):
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['status', 'priority', 'due_date']
    ordering_fields = ['due_date', 'priority']
    
    def get_queryset(self):
        return self.request.user.tasks.all()
    
    @action(detail=True, methods=['patch'])
    def mark_status(self, request, pk=None):
        task = self.get_object()
        status_value = request.data.get('status')
        if status_value not in ['Completed', 'Pending']:
            return Response({"error": "Invalid status value. Must be 'Completed' or 'Pending'."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(task, data={"status": status_value}, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
class UserRegistrationViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserRegistration
    authentication_classes = ()
    permission_classes = ()
    
    
    def create(self, request):
        serializer = UserRegistration(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
   
    
    
    

