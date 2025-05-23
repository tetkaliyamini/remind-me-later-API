"""
URL configuration for remind_me_later project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('reminders.urls')),
]
