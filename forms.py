from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextField, validators, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from models import Breakfast

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')

class BreakfastForm(FlaskForm):
    name = StringField()
    burger = SelectField('Burger', choices = [(0,'0'),(1, '1'), 
          (2, '2'), (3, '3'), (4,'4'), (5, '5'), (6, '6')])
    cheese = SelectField('Cheese DanBing', choices = [(0,'0'),(1, '1'), 
          (2, '2'), (3, '3')])
    bacon = SelectField('Bacon DanBing', choices = [(0,'0'),(1, '1'), 
          (2, '2'), (3, '3')])
    hashbrown = SelectField('Hash Brown DanBing', choices = [(0,'0'),(1, '1'), 
          (2, '2'), (3, '3'), (4,'4'), (5, '5'), (6, '6')])
    submit = SubmitField("Send")

class LunchForm(FlaskForm):
    name = StringField()
    fries = SelectField('French Fries', choices = [(0,'0'),(1, '1'), 
          (2, '2'), (3, '3'), (4,'4'), (5, '5'), (6, '6')])
    submit = SubmitField("Send")

class TeaForm(FlaskForm):
    name = StringField()
    milktea = SelectField('Bubble Milk Tea', choices = [(0,'0'),(1, '1'), 
          (2, '2'), (3, '3')])
    passionfruit = SelectField('Passion Fruit Tea', choices = [(0,'0'),(1, '1'), 
          (2, '2'), (3, '3')])
    submit = SubmitField("Send")