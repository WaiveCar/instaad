from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import current_user, login_required, logout_user
import json
import requests
from website import db
from website.campaigns.forms import SettingsForm
from website.config import config
from website.models import Campaign
import pdb


campaigns = Blueprint('campaigns', __name__)

@campaigns.route("/campaign", methods =['GET','POST'])
#@login_required
def campaign():
    if current_user.is_active == False:
        return(redirect(url_for('main.home')))
    campaign = campaign_retrieve(current_user.id)
    settings = SettingsForm()
    print("settings")
    print(settings)
    if campaign == "home":
        return redirect(url_for('users.logout'))
    if settings.validate_on_submit():
        print("here")
        print(settings.control_content.data)
        if settings.control_content.data != None:
            campaign.sett_control_content = settings.control_content.data
        if settings.business.data != None:
            campaign.sett_business = settings.business.data
        if settings.important.data == None:
            campaign.sett_social = settings.important.data 
        db.session.commit()
        return (redirect(url_for('campaigns.campaign')))
    return (render_template('campaign.html', settings = settings, campaign = campaign,title='WaiveAd'))

def campaign_retrieve(username):
    campaign = Campaign.query.filter_by(user_id=username).first()
    if campaign == None:
        return "home"
    print(campaign)
    ig_username = campaign.ig_username
    url = "http://staging.waivescreen.com/api/campaign_history?ref_id="+ig_username
    req = requests.get(url)
    campaign_db = req.text
    campaign_json = json.loads(campaign_db)
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
        return campaign
