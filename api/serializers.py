from datetime import datetime
from time import timezone
from rest_framework import serializers
from .models import *

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        
    def update(self, instance, validated_data):
        # Prevent editing if the task is completed
        if instance.status == 'Completed' and validated_data.get('status') != 'Pending':
            raise serializers.ValidationError("Completed tasks cannot be edited unless reverted to 'Pending'.")

        # Handle status update and set timestamp
        if validated_data.get('status') == 'Completed':
            instance.completed_at = datetime.now()
        elif validated_data.get('status') == 'Pending':
            instance.completed_at = None

        return super().update(instance, validated_data)
        
class UserRegistration(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8)
    
    class Meta:
        model = User
        fields = ['username', 'password']
        
    
        
