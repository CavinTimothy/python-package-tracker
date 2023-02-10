import os

from flask import Flask, render_template, redirect, url_for
from flask_migrate import Migrate
from app.config import Config
from app.shipping_form import ShippingForm

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
  # return render_template('index.html')
  return 'Package Tracker'

@app.route('/new_package', methods=['GET', 'POST'])
def new_package():
  form = ShippingForm()
  if form.validate_on_submit():
    data = form.data
    # new_package =
    print('Form is Valid')
    return redirect('/')

  return render_template('shipping_request.html', form=form)
