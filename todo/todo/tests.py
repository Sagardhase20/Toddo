from django.contrib.auth.models import User
from django.test import TestCase


class LoginFlowTests(TestCase):
    def setUp(self):
        self.username = 'testuser'
        self.email = 'testuser@example.com'
        self.password = 'Valid-pass-123'
        User.objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password,
        )

    def test_successful_login_opens_todo_page(self):
        response = self.client.post(
            '/login/',
            {'username': self.username, 'password': self.password},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'My Todo List')
        self.assertEqual(response.request['PATH_INFO'], '/todo/')

    def test_successful_email_login_opens_todo_page(self):
        response = self.client.post(
            '/login/',
            {'username': self.email, 'password': self.password},
            follow=True,
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'My Todo List')
        self.assertEqual(response.request['PATH_INFO'], '/todo/')
