from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from map.map import map

class Package(FlaskForm):
  sender_name = StringField('Sender name', validators=[DataRequired()])
  recipient_name = StringField('Recipient name', validators=[DataRequired()])
  orgin = SelectField('Origin', validators=[DataRequired()], choices=map)
  destination = SelectField('Destination', validators=[DataRequired()], choices=map)
  is_express = BooleanField('Express?', validators=[DataRequired()])
  submit = SubmitField('Ship Package')
