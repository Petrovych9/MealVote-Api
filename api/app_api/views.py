from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from .models import Restaurant
from .serializers import RestSerializer


# Create your views here.


class RestaurantAPIView(APIView):  # RestaurantAPIView
    def get(self, request):
        lst = Restaurant.objects.all().values()
        return Response({'all restaurants': list(lst)})

    def post(self, request):
        new_restaurant = Restaurant.objects.create(
            name=request.data['name'],
            address=request.data['address']
        )
        return Response({'new restaurant': model_to_dict(new_restaurant)})


# class RestAPIView(generics.ListAPIView):
#     queryset = Restaurant.objects.all()
#     serializer_class = RestSerializer


@api_view(['GET'])
def get_data(request):
    person = {'name': 'Denn', 'age': 28}
    return Response(person)
