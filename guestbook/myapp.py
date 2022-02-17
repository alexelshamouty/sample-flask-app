from flask import flash, redirect, render_template, request

from guestbook import app, db, metrics
from guestbook.forms import AddReviewForm, LoginForm
from guestbook.models import Reviews, User


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/guestbook")
def guestbook():
    reviews = Reviews.query.all()
    return render_template("list_review.html", reviews=reviews)


@app.route("/login", methods=["GET", "POST"])
@metrics.counter(
    "numer_of_logins",
    "Number of logins",
)
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        return redirect("/guestbook")
    return render_template("login.html", form=form)


@app.route("/addreview", methods=["GET", "POST"])
@metrics.gauge("in_progress_adding_review", "Long running requests in progress")
def add_review():
    form = AddReviewForm()
    if form.validate_on_submit():
        flash("We will submit your book review! thank you")
        book_name = form.book_name.data
        review = form.review.data
        new_review = Reviews(book_name=book_name, review=review)
        db.session.add(new_review)
        db.session.commit()
        Reviews(book_name=book_name, review=review)
        return redirect("/")
    return render_template("add_review.html", form=form)


@app.route("/debug-sentry")
def trigger_error():
    division_by_zero = 1 / 0


if __name__ == "__main__":
    app.run(host="0.0.0.0")
