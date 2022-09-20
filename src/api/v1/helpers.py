"""
Helper functions
"""
from decouple import config
import requests


class WeatherAPIHelper:

    @staticmethod
    def get_median(temp_list):
        half = len(temp_list) // 2
        temp_list.sort()
        if not len(temp_list) % 2:
            return (temp_list[half - 1] + temp_list[half]) / 2.0
        return temp_list[half]

    @staticmethod
    def get_forecast(city, days):
        url = config('WEATHER_API', '')
        key = config('API_KEY', '')
        weather_url = url + 'key={}'.format(key) + '&q={}'.format(city) + '&days={}'.format(days)
        err = False
        try:
            forecast = requests.get(weather_url).json()
            error = forecast.get('error', None)
            if error:
                err = True
                forecast = error.get('message', '')
        except Exception as error:
            forecast = error
            err = True
        if not err:
            forecast = forecast['forecast']['forecastday']
        return err, forecast

    @staticmethod
    def get_temperatures(forecast):
        avg_temps = []
        min_temps = []
        max_temps = []
        for date in forecast:
            day_temps = date['day']
            max_temps.append(day_temps['maxtemp_c'])
            min_temps.append(day_temps['mintemp_c'])
            avg_temps.append(day_temps['avgtemp_c'])
        return (
            max(max_temps),
            min(min_temps),
            sum(avg_temps) / len(avg_temps),
            WeatherAPIHelper.get_median(avg_temps)
        )
