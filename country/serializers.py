from rest_framework import serializers

from .models import Country, State, City


class CountrySerializer(serializers.ModelSerializer):
    """Сериализация страны"""
    class Meta:
        model = Country
        fields = ('id', 'name')


class StateSerializer(serializers.ModelSerializer):
    """Сериализация штата"""
    class Meta:
        model = State
        fields = ('id', 'name')


class CitySerializer(serializers.ModelSerializer):
    """Сериализация города"""
    class Meta:
        model = City
        fields = ('id', 'name')
