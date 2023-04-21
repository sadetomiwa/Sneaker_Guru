from flask import Flask
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from newscatcherapi import NewsCatcherApiClient

from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)



db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
newscatcherapi = NewsCatcherApiClient(x_api_key=app.config['NEWSCATCHER_API_KEY'])

from app import routes, models


