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
                return redirect(next_page) if next_page else redirect(url_for('campaigns.campaign'))
        return (render_template('index.html', form = form, title='WaiveAd'))

