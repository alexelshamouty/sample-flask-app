from os import environ

import sentry_sdk
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from prometheus_flask_exporter import PrometheusMetrics
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

SENTRY_DSN = os.environ.get("SENTRY_DSN")

if SENTRY_DSN:
    sentry_sdk.init(
        dsn=f"{SENTRY_DSN}",
        integrations=[FlaskIntegration()],
        traces_sample_rate=1.0,
    )


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
metrics = PrometheusMetrics(app)
