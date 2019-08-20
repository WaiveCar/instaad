from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required, logout_user
import json
import requests
from website import db
from website.models import Campaign
from website.config import config


campaigns = Blueprint('campaigns', __name__)

@campaigns.route("/campaign")
@login_required
def campaign():
    campaign = campaign_retrieve(current_user.id)
    if campaign == "home":
        return redirect(url_for('users.logout'))
    return (render_template('campaign.html', campaign = campaign,title='WaiveAd'))

def campaign_retrieve(username):
    campaign = Campaign.query.filter_by(user_id=username).first()
    if campaign == None:
        return "home"
    print(campaign)
    ig_username = campaign.ig_username
    url = "http://staging.waivescreen.com/api/campaign_history?ref_id="+ig_username
    print(url)
    req = requests.get(url)
    campaign_db = req.text
    campaign_json = json.loads(campaign_db)
    print(campaign_json['ref_id'])
    if campaign.lat != None and (round(campaign_json['lat'],2) == round(campaign.lat,2) or round(campaign_json['lng'],2) == round(campaign.lng,2)):
        return campaign
    else:
        campaign.lat = campaign_json['lat']
        campaign.lng = campaign_json['lng']
        url = "https://api.opencagedata.com/geocode/v1/json?q="+str(campaign_json['lat'])+","+str(campaign_json['lng'])+"&pretty=1&key=af0c0f848c3647ed9ed39e8f9747f0b3"
        req = requests.get(url)
        addr_json = json.loads(req.text)
        addr_json = addr_json['results']
        city = addr_json[0]
        city = city['components']
        city = city['suburb']
        campaign.last_city = city
        print(city)
        db.session.commit()
        #city = addr_json['components']['suburb']
        #print(city)
        return campaign
