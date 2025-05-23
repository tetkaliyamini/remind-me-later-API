from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Reminder
from .serializers import ReminderSerializer

class ReminderListCreateView(APIView):
    """API view to create a new reminder and list all reminders"""
    
    def get(self, request):
        """Handle GET requests to list all reminders"""
        reminders = Reminder.objects.all()
        serializer = ReminderSerializer(reminders, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        """Handle POST requests to create a new reminder"""
        serializer = ReminderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
