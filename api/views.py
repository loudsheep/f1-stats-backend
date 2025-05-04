import json
import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .services.schedule import get_events_remaining, get_event_schedule


@api_view(['GET'])
def schedule_remaining(request):
    return Response(json.loads(get_events_remaining()))


@api_view(['GET'])
def event_schedule(request):
    return Response(json.loads(get_event_schedule(datetime.datetime.now().year)))
