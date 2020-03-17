# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
partners class module
"""
from shapely.geometry import Point
from shapely.geometry import Polygon
from mods import mongo_module


class Partner:
    """
    test
    """
    def __init__(self, partner=None, partner_id=None, lng=None, lat=None):
        self.debug = True
        self.partner = partner if partner else None
        self.partner_id = partner_id if partner_id else None
        self.lng = lng if lng else None
        self.lat = lat if lat else None

    def partner_create(self):
        """
        test
        :param partner:
        :return:
        """
        try:
            mongo_module.mongo_insert(self.partner)
            output = 'sucesfully created'
            code = 201
        except Exception as err:
            output = str(err)
            code = 409
        return output, code

    def partner_get(self):
        """
        test
        :param id:
        :return:
        """
        try:
            document = mongo_module.mongo_find(self.partner_id, single=True)
            output = 'partner' if document else 'No data match'
            code = 200 if document else 204
        except Exception as err:
            document = None
            output = str(err)
            code = 400
        return output, document, code

    def partner_search(self):
        """
        test
        :param lng:
        :param lat:
        :return:
        """
        point = Point(self.lng, self.lat)
        try:
            partners_data = mongo_module.mongo_find({})
            closest = self.partner_find_closest(point, partners_data) if partners_data else None
            output = 'nearest partner' if partners_data else 'No data match'
            code = 200 if partners_data else 204
        except Exception as err:
            closest = None
            output = str(err)
            code = 400
        return output, closest, code

    def partner_find_closest(self, point, partners_data):
        """
        set point from lnt, lat. iter over documents from partners_data
        and get distancec fron point.
        finally get min distance fron partners_data and return lower value
        :param lng: double.
        :param lat: double
        :param partners_data: array of objects
        :return:
        """
        distance = {}
        for partner in partners_data:
            if 'coverageArea' in partner and 'coordinates' in partner['coverageArea']:
                for coordinates_array in partner['coverageArea']['coordinates']:
                    for coordinates in coordinates_array:
                        if partner['id'] in distance:
                            dist = distance[partner['id']]
                            dist.append(point.distance(Polygon(coordinates)))
                            distance[partner['id']] = dist
                        else:
                            distance[partner['id']] = [point.distance(Polygon(coordinates))]
        key = min(distance, key=distance.get) if distance else None

        return next((partner for partner in partners_data if partner['id'] == key), None)
