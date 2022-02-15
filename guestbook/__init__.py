from os import environ

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

SENTRY_DSN = os.environ.get("SENTRY_DSN")

if SENTRY_DSN:
    sentry_sdk.init(
        dsn=f"{SENTRY_DSN}",
        integrations=[FlaskIntegration()],

        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=1.0,

        # By default the SDK will try to use the SENTRY_RELEASE
        # environment variable, or infer a git commit
        # SHA as release, however you may want to set
        # something more human-readable.
        # release="myapp@1.0.0",
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
