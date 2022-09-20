""" Get location temperature """
from rest_framework import status
from rest_framework.renderers import (JSONRenderer)
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response

from .serializers import WeatherSerializer
from src.api.v1.helpers import WeatherAPIHelper


class WeatherViewSet(ViewSet):
    """ Weather viewset. """

    serializer_class = WeatherSerializer
    renderer_class = JSONRenderer

    def list(self, request, city):
        """
        Get temperature.
        -------
        If successful:
            A response payload with:
            - status code: 200
            - data
            The data is temperature object.
        If unsuccessful:
            A response payload with:
            - status code: 200
            - object with error
        Request
        -------
        method: get
        url: /api/locations/<str:city>/?days={}
        """
        days = request.query_params.get('days', 0)
        err, forecast = WeatherAPIHelper.get_forecast(city, days)
        if err:
            return Response({
                'status': 'failure',
                'data': forecast
            })
        maximum, minimum, average, median = WeatherAPIHelper.get_temperatures(forecast)
        temperature = {
            "maximum": maximum,
            "minimum": minimum,
            "average": average,
            "median": median
        }
        serializer = WeatherSerializer(temperature)
        return Response(serializer.data, status=status.HTTP_200_OK)
