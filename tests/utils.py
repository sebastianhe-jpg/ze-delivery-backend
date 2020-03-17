# -*- coding: utf-8 -*-
# !/usr/bin/env python3
import json
import time


def print_test_time_elapsed(method):
    """
    Utility method for print verbalizing test suite, prints out
    time taken for test and functions name, and status
    """
    def run(*args, **kw):
        ts = time.time()
        print('\n\ttesting function %r' % method.__name__)
        method(*args, **kw)
        te = time.time()
        print('\t[OK] in %r %2.2f sec' % (method.__name__, te - ts))
    return run


def is_json(myjson):
    try:
        json_object = json.loads(myjson)
    except (ValueError, e):
        return False
    return True
