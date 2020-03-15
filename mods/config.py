# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
enviroment vars
"""

from os import environ
from os.path import join
from os.path import dirname
from dotenv import load_dotenv

DOTENV_PATH = join(dirname(__file__), './.env')
load_dotenv(DOTENV_PATH)

LOCAL_PATH = environ.get('LOCAL_PATH')

# MONGO DB
MONGO_URL = environ.get('MONGO_URL')
MONGO_DB = environ.get('MONGO_DB')
MONGO_COL = environ.get('MONGO_COL')
