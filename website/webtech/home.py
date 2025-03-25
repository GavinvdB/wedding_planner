from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    # render de template Basic.html
    return "<h1>Weddingplanner Blooming Days.</h1>"

if __name__ == "__main__":
    app.run()