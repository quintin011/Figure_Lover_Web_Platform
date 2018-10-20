import os
from flask-wtf import csrf

class Config(object):
    SECRET_KEY=os.environ.get('SECRET_KEY')or 'you-will-never-guess'