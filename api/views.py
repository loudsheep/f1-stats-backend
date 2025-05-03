from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .services.schedule import get_events_remaining


@api_view(['GET'])
def test_route(request):
    return Response(get_events_remaining())
