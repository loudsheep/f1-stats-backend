import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.services.fastf1.schedule import get_events_remaining, get_event_schedule
from api.services.fastf1.standings import get_drivers_standings, get_constructors_standings
from api.services.fastf1.whocanwin import who_can_still_win
from api.services.fastf1.circuit import get_circut_info


@api_view(['GET'])
def events_remaining(request):
    return Response(get_events_remaining())


@api_view(['GET'])
def events_schedule(request):
    return Response(get_event_schedule(datetime.datetime.now().year))


@api_view(['GET'])
def drivers_standings(request):
    return Response(get_drivers_standings(datetime.datetime.now().year))


@api_view(['GET'])
def constructors_standings(request):
    return Response(get_constructors_standings(datetime.datetime.now().year))


@api_view(['GET'])
def possible_winners(request):
    return Response(who_can_still_win())


@api_view(['GET'])
def circuit_info(request, circuit_id):
    return Response(get_circut_info(circut_id=circuit_id))
