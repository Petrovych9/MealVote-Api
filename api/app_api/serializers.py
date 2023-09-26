from rest_framework import serializers
from .models import Restaurant


# class RestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Restaurant
#         fields = ('name', 'address')

class RestSerializer(serializers.Serializer):
    name = serializers.CharField()
    address = serializers.CharField()

    def create(self, validated_data):
        return Restaurant.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance