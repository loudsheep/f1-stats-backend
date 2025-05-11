from django.urls import path
from .views import events_remaining, events_schedule, drivers_standings, constructors_standings

urlpatterns = [
    path('remaining/', events_remaining, name="remaining"),
    path('schedule/', events_schedule, name="schedule"),
    path('standings/drivers/', drivers_standings, name="drivers.standings"),
    path('standings/constructors/', constructors_standings, name="drivers.constructors"),
]
