# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
generic validation module for flask calls.
"""


def validate_keys(request, expected, key_datatype=None):
    """
    validate input json keys
    :param request: json input
    :param expected: array of keys expected on request
    :param key_datatype: dict of key: datatype to be validated
    :return: if invalid return true; false
    """
    invalid = False
    heads = request.json.keys()
    reason = None
    if not all(elem in heads for elem in expected):
        invalid = True
        reason = "keys missing on request"
    else:
        if key_datatype:
            for key, value in key_datatype.items():
                if not isinstance(request.json[key], value):
                    invalid = True
                    reason = "incorrect datatype"

    return invalid, reason
