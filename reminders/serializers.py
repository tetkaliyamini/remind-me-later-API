from rest_framework import serializers
from .models import Reminder

class ReminderSerializer(serializers.ModelSerializer):
    """Serializer for the Reminder model"""
    class Meta:
        model = Reminder
        fields = ['id', 'date', 'time', 'message', 'method', 'created_at']
        read_only_fields = ['id', 'created_at']
    
    def validate_method(self, value):
        """Validate that method is either 'Email' or 'SMS'"""
        if value not in ['Email', 'SMS']:
            raise serializers.ValidationError("Method must be either 'Email' or 'SMS'")
        return value
    
    def validate(self, data):
        """Validate that all required fields are provided"""
        required_fields = ['date', 'time', 'message', 'method']
        for field in required_fields:
            if field not in data:
                raise serializers.ValidationError(f"{field} is required")
        return data
