import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Get absolute path to the project root
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
templates_dir = os.path.join(project_root, 'templates')
static_dir = os.path.join(project_root, 'static')

app = Flask(__name__, 
            template_folder=templates_dir, 
            static_folder=static_dir)

# Configure the database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, '../data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Configure login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
