from flask import Blueprint, Flask, render_template, redirect, url_for, session, flash, request
from BloomingDays import db
from flask_login import login_user, login_required, logout_user
from BloomingDays.admin.models import User, ContactDatabase
from BloomingDays.forms import LoginForm, RegistrationForm, ContactForm

user_blueprint = Blueprint('user',
                             __name__,
                             template_folder='templates')

@user_blueprint.route("/services")   
def services():
    #Dienstenpagina (wat leveren ze, link naar contactpagina)
    return render_template("services.html") 

@user_blueprint.route("/contact", methods=['GET', 'POST']) 
def contact():
    form = ContactForm()

    if form.validate_on_submit():
        session['voornaam'] = form.voornaam.data
        session['achternaam'] = form.achternaam.data
        session['gender'] = form.gender.data
        session['telefoon'] = form.telefoon.data
        session['email'] = form.email.data
        session['tekst'] = form.tekst.data
        
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
        return redirect(url_for('home'))  
        
    return render_template("contact.html", form=form)

@user_blueprint.route('/login', methods=['GET', 'POST'])
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
                next_page = url_for('admin.welkom')
                
            print(f"Redirecting to: {next_page}")
            return redirect(next_page)
        else:
            print("Invalid credentials")
            flash('Ongeldige email of wachtwoord.')
    else:
        if form.errors:
            print(f"Form validation errors: {form.errors}")
    
    return render_template('login.html', form=form)

@user_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        db.session.add(user)
        db.session.commit()
        flash('Dank voor de registratie. Er kan nu ingelogd worden! ')
        return redirect(url_for('admin.login'))
    return render_template('register.html', form=form)

