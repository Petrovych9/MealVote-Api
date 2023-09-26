from rest_framework import serializers
from .models import Restaurant, Employee, Menu, Vote


class RestSerializer(serializers.ModelSerializer):
    """
        Serializer for the Restaurant model.

        Fields:
        - name (str): The name of the restaurant.
        - address (str): The address of the restaurant.
        """
    class Meta:
        model = Restaurant
        fields = ('name', 'address')


class EmployeeSerializer(serializers.ModelSerializer):
    """
       Serializer for the Employee model.

       Fields:
       - name (str): The name of the employee.
       - email (str): The email address of the employee.
       """
    class Meta:
        model = Employee
        fields = ('name', 'email')


class MenuSerializer(serializers.ModelSerializer):
    """
      Serializer for the Menu model.

      Fields:
      - restaurant (int): The ID of the associated restaurant.
      - date (date): The date on which the menu is available.
      - items (json): A list of items available in the menu.
      """
    class Meta:
        model = Menu
        fields = ('restaurant', 'date', 'items')


class VoteSerializer(serializers.ModelSerializer):
    """
        Serializer for the Vote model.

        Fields:
        - employee (int): The ID of the employee who cast the vote.
        - menu (int): The ID of the menu for which the vote is cast.
        """
    class Meta:
        model = Vote
        fields = ('employee', 'menu')
