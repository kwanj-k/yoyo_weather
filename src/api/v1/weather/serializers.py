# rest_framework
from abc import ABC

from rest_framework import serializers


class WeatherSerializer(serializers.Serializer):
    maximum = serializers.DecimalField(decimal_places=2, max_digits=4)
    minimum = serializers.DecimalField(decimal_places=2, max_digits=4)
    average = serializers.DecimalField(decimal_places=2, max_digits=4)
    median = serializers.DecimalField(decimal_places=2, max_digits=4)