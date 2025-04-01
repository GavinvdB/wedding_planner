from flask import Flask, render_template, session, redirect, url_for, session
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, RadioField, SelectField, TextAreaField, SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mijngeheimesleutel'



@app.route("/")
def home():
    #Homepagina/Over ons/nav bar naar andere paginas.
    return render_template("home.html")

@app.route("/diensten")   
def diensten():
    #Dienstenpagina (wat leveren ze, link naar contactpagina)
    return render_template("diensten.html") 

@app.route("/contact") 
def contact():
    #contactpagina (contactmogelijk + afspraken maken)
    return render_template("contact.html")

@app.route("/login", methods=['GET', 'POST'])
def login(): #loginpagina voor databases
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)

