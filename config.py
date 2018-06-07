# default config
import os


class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'cbbfvfjjfjjjfsjajjkkvsjh4636787531r9898298981'
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'
    # Works for local application but not for deploying to Heroku
    #SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']  # Works for Heroku.
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:baraka@localhost/posts_dev'


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
