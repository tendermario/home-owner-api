from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import User


class AuthTestCase(APITestCase):
    """Tests for the /login and /logout routes."""

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

    def test_logout(self):
        """POSTing to /logout kills your session."""
        self.test_login()

        url = reverse('logout')
        response = self.client.post(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Logout works by setting cookie expiry to UNIX time 0 (Jan 1 1970)
        self.assertIn('Jan 1970', response.cookies['sessionid']['expires'])
