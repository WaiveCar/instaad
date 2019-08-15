from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class InstagramLogInForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('Promote me now!')

