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
        all_restaurants = Restaurant.objects.all().values()
        return Response({'all restaurants': RestSerializer(all_restaurants, many=True).data})

    def post(self, request):
        serial = RestSerializer(data=request.data)
        serial.is_valid(raise_exception=True)
        serial.save()

        new_restaurant = Restaurant.objects.create(
            name=request.data['name'],
            address=request.data['address']
        )
        return Response({'new restaurant': serial.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({"error": "Method PUT does not allowed"})
        try:
            instance = Restaurant.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exist"})

        serial = RestSerializer(data=request.data, instance=instance)
        serial.is_valid(raise_exception=True)
        serial.save()
        return Response({"restaurant": serial.data})


# class RestAPIView(generics.ListAPIView):
#     queryset = Restaurant.objects.all()
#     serializer_class = RestSerializer
