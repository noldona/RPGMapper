import logging

from flask import request, jsonify

from api.app import app, db


logger = logging.getLogger(__name__)


@app.route('/', methods=['GET'])
def index():
    return "Hello World!"


@app.route('/campaigns/', methods=['GET'])
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


@app.route('/campaigns/', methods=['POST'])
def addCampaign():
    print(request)
    data = request.json
    item = {
        'name': data['name']
    }
    db.campaigns.insert_one(item)

    return jsonify(
        status=True,
        message='Card created!'
    ), 201
