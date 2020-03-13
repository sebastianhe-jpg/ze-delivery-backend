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
