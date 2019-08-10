from datetime import datetime
from website import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
     return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    campaigns = db.relationship('Campaign',backref='user',lazy=True)
    email = db.Column(db.String, unique = True)
    paid_user = db.Column(db.Boolean, default = False)
    id = db.Column(db.Integer, primary_key = True)
    instagram = db.Column(db.String)
    password = db.Column(db.String(60), nullable = True)
    def __repr__(self):
        return f"User('{self.email}','{self.instagram}')"

class Campaign(db.Model):
    content_link = db.Column(db.String(30))
    date_paid = db.Column(db.DateTime)
    date_registered = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    date_started = db.Column(db.DateTime, nullable = True)
    id = db.Column(db.Integer, primary_key= True)
    last_city = db.Column(db.String)
    paid = db.Column(db.Boolean, default = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    def __repr__(self):
        return f"Campaign('{self.id}','{self.user_id}', '{self.date_registered}','{self.content}')"
