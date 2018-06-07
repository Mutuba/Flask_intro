from flask_testing import TestCase

from project import app, db
from project.models import User, BlogPost


class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object('config.TestConfig')
        # self.app = app.test_client()
        return app

    def setUp(self):
        db.create_all()
        db.session.add(User("Dan", "ad@min.com", "baraka"))
        db.session.add(
            BlogPost("Test post", "This is a test. Only a test.", "Dan"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
