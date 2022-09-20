"""Checks status of backend api."""

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class ApiStatusViewSet(ViewSet):
    """Status api viewset."""

    renderer_classes = (
        JSONRenderer,
        BrowsableAPIRenderer,
    )
    permission_classes = (AllowAny,)

    def get_status(self, request):
        """
        Get the status of the API.

        If it's successful, response payload with:
            - status: 200
            - data
        """
        data = {
            "status": "success",
            "message": "API works as expected.",
        }
        return Response(data, status=status.HTTP_200_OK)
