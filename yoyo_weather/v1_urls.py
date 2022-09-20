"""Version 1 URLs configuration file."""
from django.urls import path, include, re_path

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path("", include("src.api.v1.weather.urls")),
    re_path("doc_schema/", SpectacularAPIView.as_view(), name="schema"),
    re_path("docs", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
