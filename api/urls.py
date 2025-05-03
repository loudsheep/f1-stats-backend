from django.urls import path
from .views import test_route

urlpatterns = [
    path('test/', test_route, name="test"),
]
