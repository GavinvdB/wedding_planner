from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from wtforms import (StringField, SelectField, TextAreaField, 
                     BooleanField, SubmitField, TelField, 
                     EmailField, PasswordField, IntegerField)
from BloomingDays.admin.models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Inloggen')
    
class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo('pass_confirm',    message='Passwords Must Match!')])
    pass_confirm = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Leg vast!')

    def check_email(self, field):
        # Check of het e-mailadres al in de database voorkomt!
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Dit e-mailadres staat al geregistreerd.')

    def check_username(self, field):
        # Check of de gebruikersnaam nog niet vergeven is!
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Deze gebruikersnaam wordt al gebruikt, kies een andere gebruikersnaam.')
        
class ContactForm(FlaskForm):

    voornaam = StringField('Wat is uw voornaam?',validators=[DataRequired()])
    achternaam = StringField('Wat is uw achternaam?',validators=[DataRequired()])
    gender  = SelectField('Wat is uw geslacht?', choices=[('M','Man'),('V','Vrouw'),('O','Anders/Zeg liever niet'),],validators=[DataRequired()])
    telefoon = TelField('Wat is uw telefoonnummer?',validators=[DataRequired()])
    email = EmailField('Wat is uw Emailadres?',validators=[DataRequired()])
    tekst = TextAreaField()
    submit = SubmitField('Verzend')

class ListForm(FlaskForm):

    dbID = IntegerField('Vul de ID van de afspraak om meer details te bekijken:')
    submit = SubmitField('Bekijk')