from datetime import datetime
from website import db,  login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
     return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    campaigns = db.relationship('Campaign',backref='user',lazy=True)
    email = db.Column(db.String, unique = True,)
    id = db.Column(db.Integer, primary_key = True)
    instagram_auth = db.Column(db.Boolean, default = False)
    instagram = db.Column(db.String)
    password = db.Column(db.String(60), nullable = True)
    def __repr__(self):
        return f"User('{self.email}')"

class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    date_paid = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    date_started = db.Column(db.DateTime, nullable = True)
    content = db.Column(db.String(30))
    def __repr__(self):
        return f"Campaign('{self.id}','{self.user_id}', '{self.date_paid}','{self.content}')"
