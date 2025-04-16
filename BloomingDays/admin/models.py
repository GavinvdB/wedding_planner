from BloomingDays import login_manager, db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
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
        return f"{self.id}"
    
def init_db():
    db.create_all()
    
if __name__ == '__main__':
    init_db()
