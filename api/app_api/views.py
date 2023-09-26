from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Restaurant, Employee, Menu, Vote
from .serializers import RestSerializer, EmployeeSerializer, MenuSerializer, VoteSerializer
from datetime import date


# Create your views here.


class RestaurantViewSet(viewsets.ModelViewSet):
    """
       API endpoint that allows Restaurants to be viewed or edited.

       This viewset automatically provides `list`, `create`, `retrieve`,
       `update`, and `destroy` actions for Restaurants.
       """
    queryset = Restaurant.objects.all()
    serializer_class = RestSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
      API endpoint that allows Employees to be viewed or edited.

      This viewset automatically provides `list`, `create`, `retrieve`,
      `update`, and `destroy` actions for Employees.
      """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class MenuViewSet(viewsets.ModelViewSet):
    """
       API endpoint that allows Menus to be viewed or edited.

       This viewset automatically provides `list`, `create`, `retrieve`,
       `update`, and `destroy` actions for Menus.
       """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class TodaysMenusView(generics.ListAPIView):
    """
        API endpoint that lists menus available for today.

        This view returns a list of Menu objects with current date.
        """
    serializer_class = MenuSerializer

    def get_queryset(self):
        today = date.today()

        menus = Menu.objects.filter(date=today)
        return menus
