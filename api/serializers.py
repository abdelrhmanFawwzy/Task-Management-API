from rest_framework import serializers
from .models import *
import datetime



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        
        
    def validate_due_date(self, value):
        today = datetime.date.today()
        if value <= today:
            raise serializers.ValidationError("Due date must be in the future.")
        
        return value
        
    def update(self, instance, validated_data):
        
        if instance.status == 'Completed' and validated_data.get('status') != 'Pending':
            raise serializers.ValidationError("Completed tasks cannot be edited unless reverted to 'Pending'.")

        
        if validated_data.get('status') == 'Completed':
            instance.completed_at = datetime.date.today()
        elif validated_data.get('status') == 'Pending':
            instance.completed_at = None

        return super().update(instance, validated_data)
        
class UserRegistration(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8)
    
    class Meta:
        model = User
        fields = ['username', 'password']
        
    
        
