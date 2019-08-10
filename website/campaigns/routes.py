from flask import Blueprint, render_template, request
from flask_login import current_user, login_required
from website import db
from website.models import Campaign

campaigns = Blueprint('campaigns', __name__)

@campaigns.route("/campaign")
@login_required
def campaign():
    return (render_template('free_campaign.html',title='WaiveAd'))
