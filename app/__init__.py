from flask import Flask
from app.config import Config

app = Flask(__name__)

app.config.from_object(Config)

@app.route('/')
def index():
  # return render_template('index.html')
  return 'Package Tracker'

@app.route('/new_package', methods=['GET', 'POST'])
def new_package():
  return render_template('shipping_request.html')
