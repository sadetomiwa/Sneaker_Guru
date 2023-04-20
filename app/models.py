from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
# from flask_login import UserMixin



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64), nullable=False)
    last_name = db.Column(db.String(64), nullable=False)
    username = db.Column(db.String(64), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(128))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.password = generate_password_hash(kwargs.get('password'))
        db.session.add(self)
        db.session.commit()

    def check_password(self, password_guess):
        return check_password_hash(self.password, password_guess)

    def __repr__(self):
        return '<User {}>'.format(self.username)


# class Closet(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), nullable=False)
#     date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     user = db.relationship('User', backref='closets', lazy=True)
#     shoes = db.relationship('Shoe', backref='closet', lazy=True)

# class Watchlist(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(64), nullable=False)
#     date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


# class WatchlistItem(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#     shoe_id = db.Column(db.Integer, db.ForeignKey('shoe.id'), nullable=False)
#     notes = db.Column(db.String(255))

#     user = db.relationship('User', backref='watchlist_items')
#     shoe = db.relationship('Shoe', backref='watchlist_items')

# class Shoe(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     brand = db.Column(db.String(64), nullable=False)
#     model = db.Column(db.String(64), nullable=False)
#     size = db.Column(db.Integer, nullable=False)
#     condition = db.Column(db.String(64), nullable=False)
#     owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     closet_id = db.Column(db.Integer, db.ForeignKey('closet.id'))

#     def __repr__(self):
#         return '<Shoe {}>'.format(self.model)
