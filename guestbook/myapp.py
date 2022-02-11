from flask import Flask, redirect, render_template, url_for
from os import environ

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return render_template("index.html")

    @app.route("/guestbook")
    def guestbook():
        user1 = environ["USER1"]
        user2 = environ["USER2"]
        return f"<h1> will be here in a bit {user1} {user2}</h1>"

    return app

if __name__ == "__main__":
    application = create_app()
    application.run()