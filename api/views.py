import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.services.fastf1.schedule import get_events_remaining, get_event_schedule
from api.services.fastf1.standings import get_drivers_standings, get_constructors_standings


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
