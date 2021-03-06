# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
format module
"""


def output_format(description, data=None, errors=None):
    """
    generic output function
    :param description: string general output msg
    :param errors: boolean if true, return data as errors
    :param data: string/array/dict additional data for output
    :return:
    """
    outout = {
        "message": description
    }
    if errors:
        outout.update({"errors": data})
    elif data:
        if isinstance(data, (str, int, bool, float)):
            outout.update({"description": data})
        elif isinstance(data, dict):
            outout.update(data)
        else:
            outout.update({"data":data})
    return outout
