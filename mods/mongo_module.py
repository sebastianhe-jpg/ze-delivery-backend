#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mongo connection module
"""
import pymongo
from .config import MONGO_URL
from .config import MONGO_DB
from .config import MONGO_COL


def mongo_connect(collection=None):
    """
    data base connection
    :param collection: string if exist, change the collection destiny
    :return:
    """
    col = MONGO_COL
    mongo = pymongo.MongoClient(MONGO_URL)
    dbase = mongo[MONGO_DB]
    interaction = dbase[col] if collection is None else dbase[collection]
    return interaction


def mongo_find(query, filter_params=None, single=None):
    """
    find query
    :param query: json query params
    :param filter_params: json if True, add fields to show, hide. ej: {"name": 0} to hide
    :param single: boolean if True, only one interaction
    :return:
    """
    interaction = mongo_connect()
    control = {'_id': False}
    if filter_params:
        control.update(filter_params)
    if single:
        last_interaction = list(interaction.find(query, control).limit(1))
        if last_interaction:
            last_interaction = last_interaction[0]
    else:
        last_interaction = list(interaction.find(query, control))
    return last_interaction


def mongo_insert(query, collection=None, multi=None):
    """
    single/bulk insert query
    :param query: array of params to insert
    :param collection: string if exist, used to change the destiny collection
    :param multi: boolean if True, insert bulk, else insert single document
    :return:
    """
    interaction = mongo_connect(collection)
    if multi:
        return interaction.insert_many(query)
    return interaction.insert_one(query)
