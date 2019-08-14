from flask import Blueprint, render_template, redirect, request
import requests
from website.config import config

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    return (render_template('index.html',title='WaiveAd'))

@main.route("/callback/")
def callback():
    code = request.args.get('code')
    print(code)
    print(config['IG_REDIRECT_URI'])
    req = requests.post(
            'https://api.instagram.com/oauth/access_token',
            params={
                'client_id':config['IG_CLIENT_ID'],
                'client_secret':config['IG_CLIENT_SECRET'],
                'grant_type':"authorization_code",
                'redirect_uri':config['IG_REDIRECT_URI'],
                'code':code
                },
            )
    print(req.url)
    print(req.content)
    print(req.status_code)
    
    return home() 
