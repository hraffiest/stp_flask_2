import os
# - Путь к файлу БД в данной папке
db_path = 'postgresql://zion:looper@127.0.0.1:5432/mycooldb'


class Config:
    DEBUG = True
    SECRET_KEY = "asdfasdmlasdf"
    SQLALCHEMY_DATABASE_URI = db_path
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    PICTURE_PATCH = '/static/assets/pictures/'

