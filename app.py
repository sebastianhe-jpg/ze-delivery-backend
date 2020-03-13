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


@APP.route('/partner-create', methods=['POST'])
@exception_message
@cross_origin(cross_origin='*')
def partner_create():
    """

    :return:
    """
    output, code = partners_view.partner_create(request)
    return jsonify(output), code


@APP.route('/partner-get-by-id', methods=['POST'])
@exception_message
@cross_origin(cross_origin='*')
def partner_get():
    """

    :return:
    """
    output, code = partners_view.partner_get(request)
    return jsonify(output), code


@APP.route('/partner-search', methods=['POST'])
@exception_message
@cross_origin(cross_origin='*')
def partner_search():
    """

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
