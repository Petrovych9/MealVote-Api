from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Restaurant, Employee, Menu
from .serializers import RestSerializer, EmployeeSerializer, MenuSerializer
from datetime import date


# Create your views here.


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class TodaysMenusView(generics.ListAPIView):
    serializer_class = MenuSerializer

    def get_queryset(self):
        today = date.today()

        menus = Menu.objects.filter(date=today)
        return menus
