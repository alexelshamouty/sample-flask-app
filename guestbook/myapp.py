from os import environ

from flask import Flask, flash, redirect, render_template
from flask_login import LoginManager

from guestbook.forms import LoginForm


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = environ.get("SECRET_KEY")

    login = LoginManager(app)

    @app.route("/")
    def index():
        return render_template("base.html")

    @app.route("/guestbook")
    def guestbook():
        user1 = environ.get("USER1")
        user2 = environ.get("USER2")
        return render_template("list_review.html", users=[user1, user2])

    @app.route("/login", methods=["GET", "POST"])
    def login():
        # This is not checking against any source of truth .. maybe an ldap plugin or something but yeah..
        form = LoginForm()
        if form.validate_on_submit():
            username = form.username.data
            return redirect("/guestbook")
        return render_template("login.html", form=form)

    return app


if __name__ == "__main__":
    application = create_app()
    application.run()
