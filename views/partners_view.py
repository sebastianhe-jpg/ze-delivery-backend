# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
partners views module
"""
from geojson import MultiPolygon
from geojson import Point
from shapely.geometry import Polygon
from shapely.geometry import Point as xpoint
from mods import input_validator_module
from mods import sanitize_input_module
from mods import formatting_module
from mods import mongo_module


def init():
    """
    main function - test if service is up
    :return:
    """
    return formatting_module.output_format('ok'), 200


def partner_create(request):
    """
    validate input json, clean xss entry, insert document on db
    :param request: json
    :return:
    """
    invalid, reason = input_validator_module.validate_keys(request,
                                                           ['id', 'tradingName', 'ownerName',
                                                            'document', 'coverageArea',
                                                            'address'],
                                                           {"id": int},
                                                           required=True
                                                           )
    if invalid:
        return formatting_module.output_format(reason), 415

    partner_id = sanitize_input_module.entry_clean(request.json['id'])
    trading_name = sanitize_input_module.entry_clean(request.json['tradingName'])
    owner_name = sanitize_input_module.entry_clean(request.json['ownerName'])
    document = sanitize_input_module.entry_clean(request.json['document'])
    coverage_area = request.json['coverageArea']
    address = request.json['address']
    partner = {
        "id": partner_id,
        "trading_name": trading_name,
        "owner_name": owner_name,
        "document": document,
        "coverageArea": MultiPolygon(coverage_area['coordinates']),
        "address": Point(address['coordinates'])
    }

    try:
        mongo_module.mongo_insert(partner)
        output = 'sucesfully created'
        code = 201
    except Exception as err:
        output = str(err)
        code = 409
    return formatting_module.output_format(output), code


def partner_get(request):
    """
    validate input json, clean xss entry, search data on db
    :param request: json
    :return:
    """
    invalid, reason = input_validator_module.validate_keys(request,
                                                           ['id'],
                                                           {"id": int})
    if invalid:
        return formatting_module.output_format(reason), 415
    partner_id = sanitize_input_module.entry_clean(request.json['id'])
    partner_id = {"id": partner_id}
    try:
        document = mongo_module.mongo_find(partner_id, single=True)
        output = 'partner' if document else 'No data match'
        code = 200 if document else 204
    except Exception as err:
        document = None
        output = str(err)
        code = 400
    return formatting_module.output_format(output, document), code


def partner_search(request):
    """
    validate input json, clean xss entry, search data on db.
    then call find_closest partner function
    :param request: json
    :return:
    """
    invalid, reason = input_validator_module.validate_keys(request,
                                                           ['lng', 'lat'],
                                                           {'lng': float, 'lat': float})
    if invalid:
        return formatting_module.output_format(reason), 415

    lng = sanitize_input_module.entry_clean(request.json['lng'])
    lat = sanitize_input_module.entry_clean(request.json['lat'])

    try:
        partners_data = mongo_module.mongo_find({})
        closest = find_closest_partner(lng, lat, partners_data) if partners_data else None
        output = 'nearest partner' if partners_data else 'No data match'
        code = 200 if partners_data else 204
    except Exception as err:
        closest = None
        output = str(err)
        code = 400
    return formatting_module.output_format(output, closest), code


def find_closest_partner(lng, lat, partners_data):
    """
    set point from lnt, lat. iter over documents from partners_data
    and get distancec fron point.
    finally get min distance fron partners_data and return lower value
    :param lng: double.
    :param lat: double
    :param partners_data: array of objects
    :return:
    """
    point = xpoint(lng, lat)
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
    key = min(distance, key=distance.get)
    return next((partner for partner in partners_data if partner['id'] == key), None)
