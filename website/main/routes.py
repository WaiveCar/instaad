from flask import Blueprint, render_template, request

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    return (render_template('index.html',title='WaiveAd'))
@main.route("/callback")
    return redirect(url_for('home'))
