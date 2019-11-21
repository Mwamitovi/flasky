# Module to store settings for different environments
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    Default app settings.
    """
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    # instruct flask to explain how it loads templates
    EXPLAIN_TEMPLATE_LOADING = True
    # setting false to use less memory
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
    FLASKY_MAIL_SENDER = 'Flasky Admin <flasky@example.com>'
    FLASKY_ADMIN = os.getenv('FLASKY_ADMIN')

    @staticmethod
    def init_app(app):
        pass
    

class DevelopmentConfig(Config):
    """
    Settings for development env
    """
    DEBUG = True
    # app database url path is set relative to this config file
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, '../data-dev.sqlite')


class TestingConfig(Config):
    """
    Settings for testing env
    """
    TESTING = True
    # app database url path is set relative to this config file
    SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URL') or \
        'sqlite://'


class ProductionConfig(Config):
    """
    Settings for production env
    """
    # app database url path is set relative to this config file
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, '../data.sqlite')


APP_CONFIG = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}
