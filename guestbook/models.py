from flask_login import UserMixin
from guestbook import db

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(256))


class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(64))
    review = db.Column(db.Text(1024))