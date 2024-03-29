import os
# Basisverzeichnis des Projekts bestimmen
basedir = os.path.abspath(os.path.dirname(__file__))

# Konfigurationsklasse definieren
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://todoadmin:flask.2024@todoflask2024.mysql.database.azure.com:3306/todoflask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
