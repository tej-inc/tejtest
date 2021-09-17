from flask_wtf import FlaskForm 
from wtforms import StringField,PasswordField,BooleanField,SubmitField,TextAreaField
from wtforms.validators import DataRequired,Email

class login(FlaskForm):
    email = StringField("Email:", validators=[Email()])
    password = PasswordField("Password:", validators=[DataRequired()])
    submit = SubmitField("Submit")

class register(FlaskForm):
    fname = StringField("First Name:", validators=[DataRequired()])
    lname = StringField("Last Name:", validators=[DataRequired()])
    email = StringField("Email:", validators=[Email()])
    address = StringField("Address:", validators=[DataRequired()])
    country = StringField("Country:", validators=[DataRequired()])
    password = PasswordField("Password:", validators=[DataRequired()])
    password2 = PasswordField("Confirm Password:", validators=[DataRequired()])
    submit = SubmitField("Submit")

class adminlog(FlaskForm):
    email = StringField("Email:", validators=[Email()])
    password = StringField("Password:", validators=[DataRequired()])
    submit = SubmitField("Submit")

class dealerregister(FlaskForm):
    fname = StringField("First Name:", validators=[DataRequired()])
    lname = StringField("Last Name:", validators=[DataRequired()])
    email = StringField("Email:", validators=[Email()])
    address = StringField("Address:", validators=[DataRequired()])
    password = PasswordField("Password:", validators=[DataRequired()])
    password2 = PasswordField("Confirm Password:", validators=[DataRequired()])
    submit = SubmitField("Submit")


class dealerlog(FlaskForm):
    email = StringField("Email:", validators=[Email()])
    password = StringField("Password:", validators=[DataRequired()])
    submit = SubmitField("Submit")

