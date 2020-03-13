# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
generic validation module for flask calls.
"""


def validate_keys(request, expected, childs=None):
    """
    validate input json keys
    :param request:
    :param expected:
    :return: true; false
    """
    invalid = False
    heads = [elem for elem in request.json.keys()]

    if not all(elem in heads for elem in expected):
        invalid = True

    if childs:
        for kname in childs.keys():
            heads = [elem for elem in request.json[kname]]
            if not all(elem in heads for elem in childs[kname]):
                invalid = True
    return invalid
