# -*- coding: utf-8 -*-
# !/usr/bin/env python3
from mods import formatting_module


def init():
    """
    main function - test if service is up
    :return:
    """
    return formatting_module.output_format('ok'), 200
