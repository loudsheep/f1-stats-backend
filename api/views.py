from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def test_route(request):
    return Response({"message": "ok"})
