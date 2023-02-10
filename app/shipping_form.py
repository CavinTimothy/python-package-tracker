from flask_wtf import FlaskForm
from wtforms.fields import StringField, SelectField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from map.map import map

class Package(FlaskForm):
  sender_name = StringField('Sender name', validators=[DataRequired()])
  recipient_name = StringField('Recipient name', validators=[DataRequired()])
  origin = SelectField('Origin', choices=[(city, city) for city in map.keys()], validators=[DataRequired()])
  destination = SelectField('Destination', choices=[(city, city) for city in map.keys()], validators=[DataRequired()])
  is_express = BooleanField('Express?', validators=[DataRequired()])
  submit = SubmitField('Ship Package')
  cancel = SubmitField("Cancel")