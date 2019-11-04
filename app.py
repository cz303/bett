from flask import Flask

from telebot import TeleBot

from flask_sqlalchemy import SQLAlchemy


from FreeKassa import FK

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///main.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

kassa = FK()

bot = TeleBot('85760516:AAFzUYYL8hv6smZjL6boV_PCOlg1yqYJras')

admins = [677805757]

WEBHOOK_URL = f'https://bitpif.herokuapp.com/" + TOKEN'
WEBHOOK_LISTEN = '0.0.0.0'
WEBHOOK_PORT = PORT
