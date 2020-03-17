# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
partners views module
"""
from geojson import MultiPolygon
from geojson import Point
from mods import input_validator_module
from mods import sanitize_input_module
from mods import formatting_module
# from mods import mongo_module
from mods.partners import Partner

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

    partner = Partner(partner)
    output, code = partner.partner_create()
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

    partner = Partner(partner_id=partner_id)
    output, document, code = partner.partner_get()
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

    partner = Partner(lng=lng, lat=lat)
    output, data, code = partner.partner_search()
    return formatting_module.output_format(output, data), code
