from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, BooleanField
from wtforms.validators import  Length, DataRequired, Email, EqualTo, ValidationError

import sqlalchemy as sqla
from app import db
from app.main.models import Student


class RegistrationForm(FlaskForm):
   username = StringField('Username', validators = [DataRequired()]) 
   firstname = StringField('First Name', validators = [DataRequired()])
   lastname = StringField('Last Name', validators = [DataRequired()])
   email = StringField('Email', validators = [DataRequired(), Email()])
   address = TextAreaField('Address', [Length(min=0, max=200)])
   password = PasswordField('Password', validators = [DataRequired()])
   password2 = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])

   submit = SubmitField('Submit')

   def validate_email(sef, email):
       query = sqla.select(Student).where(Student.email == email.data)
       student = db.session.scalars(query).first()
       if student is not None:
          raise ValidationError('The email already exists! Please use a different username.')

   def validate_username(self, username):
       query = sqla.select(Student).where(Student.username == username.data)
       student = db.session.scalars(query).first()
       if student is not None:
           raise ValidationError('The username already exists! Please use a different username.')


class LoginForm(FlaskForm):
    username = StringField('Username', validators = [DataRequired()]) 
    password = PasswordField('Password', validators = [DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
