from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    name = StringField('Ime', 
                validators=[DataRequired(), Length(min=2, max=20)])
    surname = StringField('Prezime',
                validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                validators=[DataRequired(), Email()])
    gender = RadioField('Spol', choices = [('Man','Musko'),('Female','Zensko')])          
    submit = SubmitField('Kreni!')

