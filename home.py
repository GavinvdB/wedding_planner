from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import (StringField, SelectField, TextAreaField, 
                     BooleanField, SubmitField, TelField, 
                     EmailField)
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mijngeheimesleutel'

class ContactForm(FlaskForm):

    voornaam = StringField('Wat is uw voornaam?',validators=[DataRequired()])
    achternaam = StringField('Wat is uw achternaam?',validators=[DataRequired()])
    gender  = SelectField('Wat is uw geslacht?', choices=[('M','Man'),('V','Vrouw'),('O','Anders/Zeg liever niet'),],validators=[DataRequired()])
    telefoon = TelField('Wat is uw telefoonnummer?',validators=[DataRequired()])
    email = EmailField('Wat is uw Emailadres?',validators=[DataRequired()])
    tekst = TextAreaField()
    checkbox = BooleanField("Wil je een nieuwsbrief krijgen?")
    submit = SubmitField('Verzend')
    
@app.route("/")
def home1():
    #Homepagina/Over ons/nav bar naar andere paginas.
    return render_template("home.html")




@app.route("/diensten")   
def diensten():
    #Dienstenpagina (wat leveren ze, link naar contactpagina)
    return render_template("diensten.html") 

@app.route("/contact", methods=['GET', 'POST']) 
def contact():
    #contactpagina (contactmogelijk + afspraken maken)
    form = ContactForm()

    if form.validate_on_submit():
        session['voornaam'] = form.voornaam.data
        session['achternaam'] = form.achternaam.data
        session['gender'] = form.gender.data
        session['telefoon'] = form.telefoon.data
        session['email'] = form.email.data
        session['tekst'] = form.tekst.data
        session['checkbox'] = form.checkbox.data
    return render_template("contact.html", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login(): 
    #loginpagina voor databases
    return render_template('login.html')



if __name__ == "__main__":
    app.run(debug=True)

