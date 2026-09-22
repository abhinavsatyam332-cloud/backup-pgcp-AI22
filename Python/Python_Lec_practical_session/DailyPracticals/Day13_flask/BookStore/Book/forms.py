# from wsgiref.validate import validator

from  flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,EmailField,PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField("username",validators= [DataRequired(), Length(min=2,max=120)])

    email  = EmailField('Email',validators = [DataRequired(),Email()])

    password = PasswordField('Password',validators=[DataRequired()])
    confirm_password = PasswordField('Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
