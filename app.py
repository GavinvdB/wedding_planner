import os
import sys
from BloomingDays import app, db, login_manager
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, url_for, session, flash, request
from flask_wtf import FlaskForm
from wtforms import (StringField, SelectField, TextAreaField, 
                     BooleanField, SubmitField, TelField, 
                     EmailField)
from wtforms.validators import DataRequired, Email
from flask_login import login_user, login_required, logout_user
from BloomingDays.models import User
from BloomingDays.forms import LoginForm, RegistrationForm
import email_validator


class ContactDatabase(db.Model):
    
    __tablename__ = "Contacten"
    id = db.Column(db.Integer,primary_key=True)
    voornaam = db.Column(db.Text)
    achternaam = db.Column(db.Text)
    gender = db.Column(db.Text)
    telefoon = db.Column(db.Text)
    email = db.Column(db.Text)
    tekst = db.Column(db.Text)
    

    def __init__(self,voornaam,achternaam,gender,telefoon,email,tekst):
        self.voornaam = voornaam
        self.achternaam = achternaam
        self.gender = gender
        self.telefoon = telefoon
        self.email = email
        self.tekst = tekst
    
    def __repr__(self):
        return f"{self.voornaam} {self.achternaam} heeft dit gestuurd: {self.tekst}"


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

@app.route('/welkom')
@login_required
def welkom():
    try:
        return render_template('welkom.html')
    except Exception as e:
        flash(f"Error rendering template: {str(e)}")
        print(f"Template error: {str(e)}")
        return redirect(url_for('home1'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Je bent nu uitgelogd!')
    return redirect(url_for('home1')) 

@app.route("/services")   
def diensten():
    #Dienstenpagina (wat leveren ze, link naar contactpagina)
    return render_template("services.html") 

@app.route("/contact", methods=['GET', 'POST']) 
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        session['voornaam'] = form.voornaam.data
        session['achternaam'] = form.achternaam.data
        session['gender'] = form.gender.data
        session['telefoon'] = form.telefoon.data
        session['email'] = form.email.data
        session['tekst'] = form.tekst.data
        session['checkbox'] = form.checkbox.data
        
        contact = ContactDatabase(
            voornaam=form.voornaam.data,
            achternaam=form.achternaam.data,
            gender=form.gender.data,
            telefoon=form.telefoon.data,
            email=form.email.data,
            tekst=form.tekst.data
        )
        db.session.add(contact)
        db.session.commit()
        
        flash('Bedankt voor je bericht! We nemen contact met je op.')
        return redirect(url_for('home1'))  
        
    return render_template("contact.html", form=form)

@app.route('/login', methods=['GET', 'POST'])
def login(): 
    form = LoginForm()
    print(f"Form submitted: {request.method == 'POST'}")
    
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        print(f"User found: {user is not None}")
        
        if user is not None:
            print(f"Password check result: {user.check_password(form.password.data)}")
        
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            print("User logged in successfully")
            flash('Succesvol ingelogd.')
            
            next_page = request.args.get('next')
            if not next_page or not next_page.startswith('/'):
                next_page = url_for('welkom')
                
            print(f"Redirecting to: {next_page}")
            return redirect(next_page)
        else:
            print("Invalid credentials")
            flash('Ongeldige email of wachtwoord.')
    else:
        if form.errors:
            print(f"Form validation errors: {form.errors}")
    
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Dank voor de registratie. Er kan nu ingelogd worden! ')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/test-redirect')
def test_redirect():
    return redirect(url_for('welkom'))

# Database initialization
def create_tables():
    db.create_all()
    print("Database tables created!")

if __name__ == "__main__":
    with app.app_context():
        create_tables()
        db.create_all()  # Create tables when app starts
    app.run(debug=True)

