import django

from rest_framework.test import APITestCase, APIClient

django.setup()


class WeatherTestCase(APITestCase):

    def test_temperatures(self):
        client = APIClient()
        response = client.get("/api/locations/nairobi/")
        self.assertIsNotNone(response.data)
        self.assertEqual(200, response.status_code)

    def test_with_invalid_city(self):
        client = APIClient()
        response = client.get("/api/locations/nairtryryrobi/")
        self.assertIsNotNone(response.data)
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.data["status"], "failure")
        self.assertEqual(response.data["data"], "No matching location found.")
