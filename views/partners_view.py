# -*- coding: utf-8 -*-
# !/usr/bin/env python3
from geojson import Point
from geojson import MultiPolygon
from mods import input_validator_module
from mods import sanitize_input_module
from mods import formatting_module
from mods import mongo_module
from shapely.geometry import Point as xpoint
from shapely.geometry import Polygon


def init():
    """
    main function - test if service is up
    :return:
    """
    return formatting_module.output_format('ok'), 200


def partner_create(request):
    """

    :param request:
    :return:
    """
    invalid, reason = input_validator_module.validate_keys(request, ['id', 'tradingName', 'ownerName',
                                                             'document', 'coverageArea', 'address'], {"id": int})
    if invalid:
        return formatting_module.output_format(invalid, reason), 415

    id = sanitize_input_module.entry_clean(request.json['id'])
    trading_name = sanitize_input_module.entry_clean(request.json['tradingName'])
    owner_name = sanitize_input_module.entry_clean(request.json['ownerName'])
    document = sanitize_input_module.entry_clean(request.json['document'])
    coverageArea = request.json['coverageArea']
    address = request.json['address']
    partner = {
        "id": id,
        "trading_name": trading_name,
        "owner_name": owner_name,
        "document": document,
        "coverageArea": MultiPolygon(coverageArea['coordinates']),
        "address": Point(address['coordinates'])
    }
    mongo_module.mongo_insert(partner)
    output, code = '200', 200
    return formatting_module.output_format(output), code


def partner_get(request):
    """

    :param request:
    :return:
    """
    invalid, reason = input_validator_module.validate_keys(request, ['id'], {"id": int})
    if invalid:
        return formatting_module.output_format(invalid, reason), 415
    id = sanitize_input_module.entry_clean(request.json['id'])
    id = {"id": id}
    a = mongo_module.mongo_find(id, single=True)
    output, code = '200', 200
    return formatting_module.output_format(output,a), code


def partner_search(request):
    """

    :param request:
    :return:
    """
    invalid, reason = input_validator_module.validate_keys(request, ['lng', 'lat'], {'lng': int, 'lat': int})
    if invalid:
        return formatting_module.output_format(invalid, reason), 415
    lng = sanitize_input_module.entry_clean(request.json['lng'])
    lat = sanitize_input_module.entry_clean(request.json['lat'])
    partners_data = mongo_module.mongo_find({})

    output, code = '200', 200
    closest = find_closest_partner(lng, lat, partners_data)
    return formatting_module.output_format(output, closest), code


def find_closest_partner(lng, lat, partners_data):
    point = xpoint(lng, lat)
    distance = {}
    for partner in partners_data:
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
