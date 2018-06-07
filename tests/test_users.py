# tests/test_users.py


import unittest
# from flask import url_for
from flask_login import current_user
from flask import request

from base import BaseTestCase
from project import bcrypt
from project.models import User


class TestUser(BaseTestCase):

    # Ensure errors are thrown during an incorrect user registration
    def test_incorrect_user_registeration(self):
        with self.client:
            response = self.client.post('register/', data=dict(
                username='Michael', email='michael',
                password='python', confirm='python'
            ), follow_redirects=True)
            self.assertIn(b'Invalid email address.', response.data)
            self.assertTrue(b'/register/', request.url)

    # Ensure id is correct for the current/logged in user
    def test_is_authenticated(self):
        with self.client:
            self.client.post('/login', data=dict(
                username="Dan", password='baraka'
            ), follow_redirects=True)
            self.assertTrue(current_user.is_authenticated)
            # self.assertFalse(current_user.id == 20)


class UserViewsTests(BaseTestCase):

    # Ensure that Flask was set up correctly
    def test_index(self):
        response = self.client.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # Ensure that the login page loads correctly
    def test_login_page_loads(self):
        response = self.client.get('/login')
        self.assertIn(b'Please login', response.data)

    # Ensure login behaves correctly with correct credentials
    def test_correct_login(self):
        with self.client:
            response = self.client.post(
                '/login',
                data=dict(username="Dan", password="baraka"),
                follow_redirects=True
            )
            # self.assert_redirects(response, url_for('home.home'))
            self.assertIn(b'You were just logged in', response.data)
            self.assertTrue(current_user.name == "Dan")
            self.assertTrue(current_user.is_active)
            self.assertTrue(current_user.is_anonymous)

    # Ensure login behaves correctly with incorrect credentials
    def test_incorrect_login(self):
        with self.client:
            response = self.client.post(
                '/login',
                data=dict(username="wrong", password="wrong"),
                follow_redirects=True
            )
            self.assertIn(
                b'Invalid Crediantial. Please try again', response.data)
            self.assertFalse(current_user.is_active)

    # Ensure logout behaves correctly
    def test_logout(self):
        with self.client:
            self.client.post(
                '/login',
                data=dict(username="Dan", password="baraka"),
                follow_redirects=True
            )
            response = self.client.get('/logout', follow_redirects=True)
            self.assertIn(b'Please login', response.data)
            self.assertFalse(current_user.is_active)

    # Ensure that logout page requires user login
    def test_logout_route_requires_login(self):
        response = self.client.get('/logout', follow_redirects=True)
        self.assertIn(b'Please log in to access this page', response.data)


if __name__ == '__main__':
    unittest.main()
