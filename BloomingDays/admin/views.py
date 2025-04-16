from flask import Blueprint, Flask, render_template, redirect, url_for, session, flash, request
from BloomingDays import db
from flask_login import login_user, login_required, logout_user
from BloomingDays.admin.models import User
from BloomingDays.forms import LoginForm

admin_blueprint = Blueprint('admin',
                             __name__,
                             template_folder='templates')

@admin_blueprint.route('/welkom')
@login_required
def welkom():
    try:
        return render_template('welkom.html')
    except Exception as e:
        flash(f"Error rendering template: {str(e)}")
        print(f"Template error: {str(e)}")
        return redirect(url_for('home1'))

@admin_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Je bent nu uitgelogd!')
    return redirect(url_for('home'))

user_blueprint = Blueprint('user',
                            __name__,
                            template_folder='templates')

@user_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()
        
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Gefeliciteerd! Inloggen gelukt!', 'success')
            return redirect(url_for('admin.welkom'))
        else:
            flash('Ongeldige inloggegevens', 'danger')
    return render_template('login.html', form=form)