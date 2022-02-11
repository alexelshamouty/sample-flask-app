from flask import Flask, redirect, render_template, url_for

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return render_template("index.html")

    @app.route("/guestbook")
    def guestbook():
        return "<h1> will be here in a bit </h1>"

    return app

if __name__ == "__main__":
    application = create_app()
    application.run()