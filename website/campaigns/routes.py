from flask import Blueprint, render_template, request
from flask_login import current_user, login_required
from website import db
from website.models import Campaign

campaigns = Blueprint('campaigns', __name__)

@campaigns.route("/campaign")
@login_required
def campaign():
    campaign = Campaign.query.filter_by(user_id=current_user.id).first()
    return (render_template('campaign.html', campaign = campaign,title='WaiveAd'))
