from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, RadioField, SelectField, Field
from wtforms.validators import DataRequired
from  wtforms.widgets import Input, Select, CheckboxInput 

class InstagramLogInForm(FlaskForm):
    username = StringField(u'Username', validators=[DataRequired()])
    submit = SubmitField('Put me on a screen in LA')
class SettingsForm(FlaskForm):
    business = RadioField(u'Business or non-business', choices=[('yes-busi','Business'),('no-busi','Non-business'),('both','Both')])
    control_content = RadioField(u'Control of Content', choices=[("owner",'I own the Instagram account'),("none-owner","The Instagram account is someone else's")])
    social = RadioField(u'Important Social Media', choices=[('newsfeed','Twitter/Facebook'),('instagram','Instagram'),('videosite','Youtube'),('reviewsite','Yelp'),('own website', 'Your website'),('aggregator','Reddit')])
    submit = SubmitField('Save')

