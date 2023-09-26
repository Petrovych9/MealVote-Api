from rest_framework import serializers
from .models import Restaurant


class RestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('name', 'address')