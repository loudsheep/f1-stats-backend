from django.urls import path
from .views import schedule_remaining, event_schedule

urlpatterns = [
    path('remaining/', schedule_remaining, name="remaining"),
    path('schedule/', event_schedule, name="schedule"),
]
