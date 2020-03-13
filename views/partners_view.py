# -*- coding: utf-8 -*-
# !/usr/bin/env python3
from geojson import Point
from geojson import MultiPolygon
from mods import input_validator_module
from mods import sanitize_input_module
from mods import formatting_module


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
    if input_validator_module.validate_keys(request, ['id', 'tradingName', 'ownerName',
                                                      'document', 'coverageArea', 'address']):
        return formatting_module.output_format('missing keys'), 415

    id = sanitize_input_module(request.json['id'])
    trading_name = sanitize_input_module(request.json['tradingName'])
    owner_name = sanitize_input_module(request.json['ownerName'])
    document = sanitize_input_module(request.json['document'])
    coverageArea = sanitize_input_module(request.json['coverageArea'])
    address = sanitize_input_module(request.json['address'])

    MultiPolygon([
        [[[30, 20], [45, 40], [10, 40], [30, 20]]],
        [[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]]
    ])
    Point([-46.57421, -21.785741])

    partner = {
        "id": id,
        "tradingName": trading_name,
        "ownerName": owner_name,
        "document": document, # uuid
        "coverageArea": MultiPolygon(coverageArea),
        "address": Point(address)
    }

    output, code = '200', 200
    return formatting_module.output_format(output), code


def partner_get(request):
    """

    :param request:
    :return:
    """
    if input_validator_module.validate_keys(request, ['id']):
        return formatting_module.output_format('missing keys'), 415
    id = sanitize_input_module(request.json['id'])

    output, code = '200', 200
    return formatting_module.output_format(output), code


def partner_search(request):
    """

    :param request:
    :return:
    """
    if input_validator_module.validate_keys(request, ['lng', 'lat']):
        return formatting_module.output_format('missing keys'), 415
    lng = sanitize_input_module(request.json['lng'])
    lat = sanitize_input_module(request.json['lat'])

    output, code = '200', 200
    return formatting_module.output_format(output), code
