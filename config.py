import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Configuration:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ADMIN_SWATCH = 'cerulean'
    SESSION_TPE = 'filesystem'
