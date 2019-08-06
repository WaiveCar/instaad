from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '84e0621dd931baa7e6a014901c6183d5'
#sqllite is for development purposes
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
print(__name__)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique = True,)
    password = db.Column(db.String(60), nullable = True)
    campaigns = db.relationship('Campaign',backref='email',lazy=True)


    def __repr__(self):
        return f"User('{self.email}')"

class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    date_paid = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    date_started = db.Column(db.DateTime, nullable = True)
    content = db.Column(db.String(30))
    def __repr__(self):
        return f"Campaign('{self.id}','{self.user_id}', '{self.date_paid}')"

#Development variable
users = [
    {
        'id' : 1,
        'email' : 'chen97me@gmail.com',
        'campaigns' : 2,
        'password' : 'password'
    },
    {
        'id' : 2,
        'email' : 'Chen97@gmail.com',
        'campaigns' : 3,
        'password' : 'password'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return (render_template('index.html'))

@app.route("/user")
def user():
    return (render_template('user.html', user_id = 1))

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data ==  users[1]['email'] and form.password.data == users[1]['password']:
            flash('You have been logged in!', 'success')
            return(redirect(url_for('home')))
        else:
            flash('Log In Unsuccessful, please check email and password', 'danger')
    return (render_template('login.html',title='Login',form=form))

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print("Form valid")
        flash(f'Account created for {form.name.data}!','success')
        return redirect(url_for('home'))
    return (render_template('register.html', title='Register',form=form))

@app.route("/campaign")
def campaigns():
    return (render_template('campaign.html'))

if __name__ == "__main__":
    app.run()
