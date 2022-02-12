from os import environ

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SECRET_KEY"] = environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://%s:%s@%s/guestbook" % (
    environ.get("MYSQL_USER"),
    environ.get("MYSQL_USER_PASSWORD"),
    environ.get("MYSQL_HOST"),
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
