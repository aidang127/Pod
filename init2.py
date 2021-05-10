import os
from flask import Flask
import flask
import login as login

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

app = flask.Flask(__name__)
app.config.from_object(Config)
app._static_folder = os.path.abspath("static/")
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = "login"
bootstrap = Bootstrap(app)

from app import routes, models, errors