import logging

from flask import request, jsonify, make_response
from flask_cors import cross_origin

from api.app import app, db


logger = logging.getLogger(__name__)


@app.route('/', methods=['GET'])
def index():
    return "Hello World!"


@app.route('/api/campaigns/', methods=['GET'])
def getCampaigns():
    _campaigns = db.campaigns.find()

    item = {}
    data = []
    for campaign in _campaigns:
        item = {
            'id': str(campaign['_id']),
            'name': campaign['name']
        }
        data.append(item)

    return jsonify(
        status=True,
        data=data
    )


@app.route('/api/campaigns/', methods=['POST'])
def addCampaign():
    data = request.json
    item = {
        'name': data['name']
    }
    db.campaigns.insert_one(item)

    return jsonify(
        status=True,
        message='Campaign created!'
    ), 201


@app.route('/api/login/', methods=['POST'])
def login():
    data = request.json
    logger.debug(data)

    return jsonify(
        status=True,
        message='Logged In!'
    ), 200

@app.after_request
def add_headers(response):
    response.headers['Content-Type'] = 'application/json'
    return response
