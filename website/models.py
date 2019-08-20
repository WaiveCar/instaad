from datetime import datetime
from website import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(id):
     return User.query.get(int(id))

def load_campaign(id):
     return Campaign.query.get(int(id))

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    campaigns = db.relationship('Campaign',backref='user',lazy=True)
    email = db.Column(db.String, unique = True)
    paid_user = db.Column(db.Boolean, default = False)
    id = db.Column(db.Integer, primary_key = True)
    password = db.Column(db.String(60), nullable = True)
    def __repr__(self):
        return f"User('{self.email}','{self.id}')"

class Campaign(db.Model):
    __tablename__ = 'campaign'
    date_registered = db.Column(db.DateTime, nullable = True)
    id = db.Column(db.Integer, primary_key= True)
    ig_username = db.Column(db.String, unique=True)
    lat = db.Column(db.Integer)
    lng = db.Column(db.Integer)
    last_city = db.Column(db.String)
    paid = db.Column(db.Boolean, default = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    def __repr__(self):
        return f"Campaign('{self.id}','{self.user_id}','{self.last_city}', '{self.date_registered}')"
