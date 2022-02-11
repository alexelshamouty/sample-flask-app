from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import BooleanField, PasswordField, StringField, SubmitField

# Could also do some more validation but let's keep it simple


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Sign in")
