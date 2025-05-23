from django.db import models

class Reminder(models.Model):
    """Model for storing reminder information"""
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()
    method = models.CharField(max_length=10, choices=[
        ('Email', 'Email'),
        ('SMS', 'SMS'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.date} {self.time}: {self.message} via {self.method}"
