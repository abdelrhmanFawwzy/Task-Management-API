from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from rest_framework.permissions import IsAdminUser
from rest_framework.authentication import TokenAuthentication

from rest_framework import viewsets, status
from .models import *
from .serializers import *

from django.shortcuts import get_object_or_404


class TaskViewSet(viewsets.ModelViewSet):
    
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filterset_fields = ['status', 'priority', 'due_date']
    ordering_fields = ['due_date', 'priority']
    
    def get_queryset(self):
        return self.request.user.tasks.all()
    
    def perform_create(self, serializer):
        serializer.save(assigned_to=self.request.user)
    
    # @action(detail=True, methods=['patch'])
    # def mark_status(self, request, pk=None):
    #     task = self.get_object()
    #     status_value = request.data.get('status')
    #     if status_value not in ['Completed', 'Pending']:
    #         return Response({"error": "Invalid status value. Must be 'Completed' or 'Pending'."}, status=status.HTTP_400_BAD_REQUEST)
    #     serializer = self.get_serializer(task, data={"status": status_value}, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
class UserRegistrationViewSet(viewsets.ModelViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserRegistration

    
    
    def get_authentication_classes(self):
        
        if self.action in 'list':
            return [TokenAuthentication()]
        return []

    def get_permissions(self):
        
        if self.action == 'list':
            return [IsAdminUser()]
        return []
    
    def create(self, request):
        serializer = UserRegistration(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        
        queryset = self.queryset
        custom_data = [
        {
            "id": user.id,
            "username": user.username,
        }
        for user in queryset
    ]
        return Response(custom_data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
       
        instance = get_object_or_404(self.queryset, pk=pk)
        if instance != request.user:
            return Response(
                {"detail": "You do not have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
   
    def update(self, request, pk=None, partial=True):
        
        instance = get_object_or_404(self.queryset, pk=pk)
        if instance != request.user:
            return Response(
                {"detail": "You do not have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        instance = get_object_or_404(self.queryset, pk=pk)
        if instance != request.user:
            return Response(
                {"detail": "You do not have permission to perform this action."},
                status=status.HTTP_403_FORBIDDEN
            )
        instance.delete()
        return Response(
            {"detail": "User deleted successfully."},
            status=status.HTTP_204_NO_CONTENT
        )
    

