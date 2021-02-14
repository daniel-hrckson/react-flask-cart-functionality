import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from models import *
import json
from utilities import *
from flask_cors import CORS
from flask import Flask, request
from math import floor
import time
from views import Views
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)
app.register_blueprint(Views)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


host = 'localhost'
port = 5000

if __name__ == '__main__':
    app.run(host= host, port= port, debug=True)
