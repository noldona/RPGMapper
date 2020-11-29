import os
import logging
import logging.config

from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS


root_path = os.path.dirname(os.path.abspath(__file__))
logging.config.fileConfig(root_path + '/config/logging.ini')
logger = logging.getLogger(__name__)
logger.info('Starting API')

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + \
    ':' + os.environ['MONGODB_PASSWORD'] + '@' + \
    os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']
mongo = PyMongo(app)
cors = CORS(app)
db = mongo.db

from api import routes
