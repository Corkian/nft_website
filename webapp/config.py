import os


class Config:
    SECRET_KEY = "mysecretkey"
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:Wingsgt13@localHost:5432/subscribers'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('mail_user')
    MAIL_PASSWORD = os.environ.get('mail_passwd')