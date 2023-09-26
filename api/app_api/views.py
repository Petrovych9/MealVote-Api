from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Restaurant
from .serializers import RestSerializer


# Create your views here.


class RestAPIView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestSerializer


@api_view(['GET'])
def get_data(request):
    person = {'name': 'Denn', 'age': 28}
    return Response(person)