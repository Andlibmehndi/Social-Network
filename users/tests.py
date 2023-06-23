from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User

class UserAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_create_user(self):
        data = {'username': 'testuser', 'password': 'testpassword'}
        response = self.client.post('/user/login/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)