from flask_wtf import FlaskForm
from wtforms.fields import StringField, TextAreaField, SubmitField, PasswordField, EmailField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'PNG','JPG','png','jpg'}

class DestinationForm(FlaskForm):
    name = StringField('Country', validators=[InputRequired()])
    description = TextAreaField('Description', validators=[InputRequired(), Length(10)])
    image = FileField('Destination Image', validators=[
        FileRequired(message = 'Image cannot be empty'),
        FileAllowed(ALLOWED_FILE, message='Only supports png, jpg, JPG, PNG')])
    currency = StringField('Currency', validators=[InputRequired()])
    submit = SubmitField('Create')


class CommentForm(FlaskForm):
    text = TextAreaField('Comment', validators=[InputRequired()])
    submit = SubmitField('Create')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    email = EmailField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Password', validators=[InputRequired()])
    confirm_password = PasswordField('Confirms password', validators=[
                                     InputRequired(), EqualTo('password', message='Please re-enter the same password')])
    submit = SubmitField('Register')
