from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, RadioField, SelectField, Field
from wtforms.validators import DataRequired
from  wtforms.widgets import Input, Select, CheckboxInput 

class InstagramLogInForm(FlaskForm):
    username = StringField(u'Username', validators=[DataRequired()])
    submit = SubmitField('Put me on a screen in LA')
class SettingsForm(FlaskForm):
    business = RadioField('Business or non-business', choices=[('yes-busi','Business'),('no-busi','Non-business'),('both','Both')])
    control_content = RadioField('Control of Content', choices=[(1,'Yes'),(0,'No')])
    social = RadioField('Important Social Media', choices=[('newsfeed','Twitter/Facebook or another newsfeed site'),('videosite','Youtube or other video sites'),('reviewsite','Yelp or another review site'),('own website', 'Your website'),('aggregator','Reddit/Producthunt or other aggregator sites')])
    submit = SubmitField('Save')

