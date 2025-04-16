from flask import Blueprint, Flask, render_template, redirect, url_for, session, flash, request, abort
from BloomingDays import db
from flask_login import login_user, login_required, logout_user, current_user
from BloomingDays.admin.models import User, ContactDatabase
from BloomingDays.forms import ListForm, VerwijderForm

admin_blueprint = Blueprint('admin',
                             __name__,
                             template_folder='templates')

@admin_blueprint.route('/dashboard')
@login_required
def welkom():
    try:
        return render_template('welkom.html')
    except Exception as e:
        flash(f"Error rendering template: {str(e)}")
        print(f"Template error: {str(e)}")
        return redirect(url_for('home'))

@admin_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Je bent nu uitgelogd!')
    return redirect(url_for('home'))

@admin_blueprint.route("/database")   
@login_required
def database():
    #homepagina van de database dat alle afspraken laat zien.
    afspraken = ContactDatabase.query.all()
    return render_template("homeDB.html",afspraken=afspraken) 

@admin_blueprint.route('/homeDB')
@login_required
def homeDB():
    if not current_user.is_admin:
        flash('You do not have permission to access this page.', 'danger')
        return redirect(url_for('home'))
    return render_template('homeDB.html')

@admin_blueprint.route("/dblist",methods=['GET', 'POST'])   
def dblist():
    #Voer de ID van het formulier waarvan je meer over wilt weten op deze pagina.
    form = ListForm()
    
    if form.validate_on_submit():
        id = form.dbID.data
        con = ContactDatabase.query.get(id)
        db.session.commit()

        return render_template("dblist.html",form=form,con=con,id=id)
    return render_template("dblist.html", form=form) 

@admin_blueprint.route("/delform", methods=['GET', 'POST'])
def delform():
    #pagina om formulieren te verwijderen
    form = VerwijderForm()
    if form.validate_on_submit():
        id = form.id.data
        formulier = ContactDatabase.query.get(id)
        db.session.delete(formulier)
        db.session.commit()

        return render_template('homeDB.html')
    return render_template("delform.html",form=form)
