from django.urls import include, path

from .views import WeatherViewSet

temperature = WeatherViewSet.as_view({
    'get': 'list'
})

urlpatterns = [
    path('locations/<str:city>/', temperature, name='temperature'),
]