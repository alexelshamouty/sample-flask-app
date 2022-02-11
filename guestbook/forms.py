from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.widgets import TextArea

# Could also do some more validation but let's keep it simple


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign in")


class AddReviewForm(FlaskForm):
    book_name = StringField("Book Name", validators=[DataRequired()])
    review = StringField(u'Review', widget=TextArea())
    submit = SubmitField("Submit review")

