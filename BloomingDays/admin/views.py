from flask import Blueprint, Flask, render_template, redirect, url_for, session, flash, request
from BloomingDays import db
from flask_login import login_user, login_required, logout_user

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