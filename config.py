
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'AIzaSyCfWDBJi5UJI1zvGoNd4THBr-IO98nmc-c'

    # Configuration
    key="AIzaSyCfWDBJi5UJI1zvGoNd4THBr-IO98nmc-c"
    GOOGLE_CLIENT_ID = '216768866079-t759biihn8ad39n3t3emp3i0c7h4r8g6.apps.googleusercontent.com'
    GOOGLE_CLIENT_SECRET = 'uV8R5Uk8GmiKGMsiOgdqdZJ0'
  