from flask import Blueprint, render_template, redirect, request
from website import config

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    return (render_template('index.html',title='WaiveAd'))

@main.route("/callback/")
def callback():
    code = request.args.get('code')
    print(code)
    print("IG_CLIENT_ID: " + IG_CLIENT_ID)
    #first_r = request.get()
    return home() 
