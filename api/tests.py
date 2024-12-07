from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import User


class LoginTestCase(APITestCase):
    """Tests for the /login route."""

    def test_login(self):
        """Ensure we can create a login session."""
        user = User(username='guy.incognito@example.com')
        user.set_password('pabopabo')
        user.save()

        url = reverse('login')
        data = {'email': user.username, 'password': 'pabopabo'}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('sessionid', response.cookies)

    def test_login_failed(self):
        """Using incorrect credentials responds with a 400 error."""
        url = reverse('login')
        data = {'email': 'guy.incognito@example.com', 'password': 'pabopabo'}

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
