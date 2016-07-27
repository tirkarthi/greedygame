
from django.test import TestCase
from rest_framework.test import APIClient
from .models import *

class MyTestCase(TestCase):

    fixtures = ['fixtures.json']

    def test_get_track(self):
        api_client = APIClient()
        req = api_client.get('/api/tracks/38')
        self.assertEqual(req.status_code, 200)
        self.assertEqual(req.data['rating'], 4)
