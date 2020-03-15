# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
partners class module
"""


class Partner:
    def __init__(self):
        self.debug = True

    def partner_create(self, partner):
        self.id = partner['id']
        self.trading_name = partner['trading_name']
        self.owner_name = partner['owner_name']
        self.document = partner['document']
        self.coverageArea = partner['coverageArea']
        self.address = partner['address']
        return

    def partner_get(self, id):
        self.id = id
        return

    def partner_search(self, lng, lat):
        self.lng = lng
        self.lat = lat
        return
