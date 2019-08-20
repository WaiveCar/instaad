from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import current_user, login_user
import requests
from website import db, login_manager
from website.config import config
from website.campaigns.forms import InstagramLogInForm
from website.models import Campaign, User

main = Blueprint('main', __name__)

@main.route("/", methods=['GET','POST'])
@main.route("/home", methods=['GET','POST'])
def home():
    if current_user.is_authenticated:
        return redirect(url_for('campaigns.campaign'))
    else:
        form = InstagramLogInForm()
        if form.validate_on_submit():
            exists=Campaign.query.filter_by(ig_username=form.username.data).first()
            if exists:
                user = User.query.filter_by(id=exists.user_id).first()
                login_user(user)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('campaigns.campaign'))
            else:
                user = User()
                db.session.add(user)
                db.session.commit()
                campaign = Campaign(ig_username = form.username.data, user_id = user.id)
                db.session.add(campaign)
                db.session.commit()
                login_user(user)
                next_page = request.args.get('next')
                campaign_submit(form.username.data)
                return redirect(next_page) if next_page else redirect(url_for('campaigns.campaign'))
        return (render_template('index.html', form = form, title='WaiveAd'))

def campaign_submit(username):
    url = "http://staging.waivescreen.com/api/campaign"
    secret = config['API_SECRET_KEY']
    ref_id = username
    asset = 'http://9ol.es/ad-new/?user='+username
    req = requests.post(url, {
        'url':url,
        'secret':secret,
        'ref_id':ref_id,
        'asset':asset})
    print("This responded with a status code of")
    print(req.status_code)
