
import unittest

from flask_login import current_user

from base import BaseTestCase
from project import bcrypt
from project.models import User


class TestUser(BaseTestCase):
    # Ensure user can register
    def test_user_registeration(self):
        with self.client:
            response = self.client.post('register/', data=dict(
                username='Michael', email='michael@realpython.com',
                password='python', confirm='python'
            ), follow_redirects=True)
            self.assertIn(b'Welcome to Flask!', response.data)
            self.assertTrue(current_user.name == "Michael")
            self.assertTrue(current_user.is_active())
            user = User.query.filter_by(email='michael@realpython.com').first()
            self.assertTrue(str(user) == '<name - Michael>')

    # Ensure id is correct for the current/logged in user
    def test_get_by_id(self):
        with self.client:
            self.client.post('/login', data=dict(
                username="Dan", password='baraka'
            ), follow_redirects=True)
            self.assertTrue(current_user.id == 1)
            self.assertFalse(current_user.id == 20)
 
    # Ensure given password is correct after unhashing
    def test_check_password(self):
        user = User.query.filter_by(email='ad@min.com').first()
        self.assertTrue(bcrypt.check_password_hash(user.password, 'baraka'))
        self.assertFalse(bcrypt.check_password_hash(user.password, 'foobar'))


if __name__ == '__main__':
    unittest.main()

