from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    username = db.Column(db.String(64), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(128))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    closet = db.relationship('Closet', backref='owner', lazy=True)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.password = generate_password_hash(kwargs.get('password'))
        db.session.add(self)
        db.session.commit()

    def check_password(self, password_guess):
        return check_password_hash(self.password, password_guess)

    def __repr__(self):
        return '<User {}>'.format(self.username)

@login.user_loader
def get_user_id(user_id):
    return User.query.get(user_id)

class Sneaker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(50), nullable=False)
    image_url = db.Column(db.String(200), nullable=True)
    price = db.Column(db.Float, nullable=True)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f'<Sneaker {self.id}>'
    

class Closet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    sneaker_id = db.Column(db.Integer, db.ForeignKey('sneaker.id'), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('closets', lazy=True))
    sneaker = db.relationship('Sneaker', backref=db.backref('closets', lazy=True))

    def __repr__(self):
        return f'<Closet {self.id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'sneaker_id': self.sneaker_id,
        }





    

