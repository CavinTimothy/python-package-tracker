import os

class Config(object):
  SECRET_KEY = os.environ.get('SECRET_KEY')
  FLASK_DEBUG = os.environ.get('FLASK_DEBUG')
