from flask import render_template
from BloomingDays import app

@app.route("/")
def home():
    #Homepagina/Over ons/nav bar naar andere paginas.
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)