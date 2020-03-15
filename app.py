# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
flask app module
"""
from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import cross_origin
from views import partners_view
from mods.decorator_module import exception_message
APP = Flask(__name__)

from mods import mongo_module

a = mongo_module.mongo_connect()
a.create_index("document", unique=True)


# --------------- partners ---------------
@APP.route('/partner-create', methods=['POST'])
@exception_message
@cross_origin(cross_origin='*')
def partner_create():
    """
    {
        "id": 1,
        "tradingName": "Adega da Cerveja - Pinheiros",
        "ownerName": "Zé da Silva",
        "document": "1432132123891/0001",
        "coverageArea": {
            "type": "MultiPolygon",
            "coordinates": [
                    [[[30, 20], [45, 40], [10, 40], [30, 20]]],
                    [[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]]
            ]
        },
        "address": {
            "type": "Point",
            "coordinates": [
                -46.57421, -21.785741
            ]
        }
    }
    :return:
    """
    output, code = partners_view.partner_create(request)
    return jsonify(output), code


@APP.route('/partner-get-by-id', methods=['POST'])
@exception_message
@cross_origin(cross_origin='*')
def partner_get():
    """
    {
        "id": 1
    }
    :return:
    """
    output, code = partners_view.partner_get(request)
    return jsonify(output), code


@APP.route('/partner-search', methods=['POST'])
@exception_message
@cross_origin(cross_origin='*')
def partner_search():
    """
    {
        "lng": -46.57421,
        "lat": -21.785741
    }
    :return:
    """
    output, code = partners_view.partner_search(request)
    return jsonify(output), code


# --------------- main ---------------
@APP.route('/')
@exception_message
@cross_origin(cross_origin='*')
def init():
    """
    landpage flask function to check if service is up
    :return:
    """
    output, code = partners_view.init()
    return jsonify(output), code


if __name__ == '__main__':
    APP.run()
