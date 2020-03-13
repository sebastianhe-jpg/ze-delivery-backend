# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
format module
"""


def output_format(description, data=None, errors=None):
    """
    generic output function
    :param description: general output msg
    :param errors: if true, return data as errors
    :param data: additional data for output
    :return:
    """
    outout = {
        "message": description
    }
    if errors:
        outout.update({"errors": data})
    elif data:
        if isinstance(data, str):
            outout.update({"description": data})
        else:
            outout.update(data)
    return outout
