from django.urls import path, re_path
from .views import events_remaining, events_schedule, drivers_standings, constructors_standings, possible_winners, \
    circuit_info, race_results

urlpatterns = [
    path('remaining/', events_remaining, name="remaining"),
    path('schedule/', events_schedule, name="schedule"),
    path('standings/drivers/', drivers_standings, name="drivers.standings"),
    path('standings/constructors/', constructors_standings, name="drivers.constructors"),
    path('standings/who-can-win/', possible_winners, name="drivers.possible_winners"),
    path('circuit/<str:circuit_id>/<int:season>/<int:round>', circuit_info, name="circuit.info"),
    re_path(r'^results/(?P<season>\d+|current)/(?P<round>\d+)/$', race_results, name="results.race"),
]
