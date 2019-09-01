# Module to store settings for different environments

import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """
    Default app settings.
    """
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    # instruct flask to explain how it loads templates
    EXPLAIN_TEMPLATE_LOADING = True    
    # app database url path is set relative to this config file
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '../data.sqlite')
    # setting false to use less memory
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    


class DevelopmentEnv(Config):
    """
    Settings for development env
    """
    DEBUG = True


APP_CONFIG = {
    "development": DevelopmentEnv,
    # "testing": TestingEnv,
    # "production": ProductionEnv
}
