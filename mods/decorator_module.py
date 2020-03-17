# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
exception decorator module
"""
from flask import jsonify
from mods import formatting_module


def exception_message(function):
    """
    A decorator that wraps the passed in function and logs
    exceptions should one occur
    """

    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as error:
            err = """There was an issue with the function %s,
            We're sorry, we got an issue right now,
            please try later.""" % function.__name__
            return jsonify(formatting_module.output_format(err, str(error), errors=True)), 415
    wrapper.__name__ = function.__name__
    return wrapper
