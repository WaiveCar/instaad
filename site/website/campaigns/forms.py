from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class InstagramLogInForm(FlaskForm):
    Username = StringField('Username', validators=[DataRequired()])
    InstagramCode = StringField('Code', validators=[DataRequired()])
