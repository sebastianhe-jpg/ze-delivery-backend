# -*- coding: utf-8 -*-
# !/usr/bin/env python3
from geojson import Point
from geojson import MultiPolygon
from mods import formatting_module


def init():
    """
    main function - test if service is up
    :return:
    """
    return formatting_module.output_format('ok'), 200


def partner_create(request):
    request
    partner = {
        "id": 1,
        "tradingName": "Adega da Cerveja - Pinheiros",
        "ownerName": "Zé da Silva",
        "document": "1432132123891/0001", # uuid
        "coverageArea": {
            # GeoJSON MultiPolygon - area of service
            "type": "MultiPolygon",
            "coordinates": [
                [[[30, 20], [45, 40], [10, 40], [30, 20]]],
                [[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]]
            ]
        },
        "address": {
            # GeoJSON Point - location partner
            "type": "Point",
            "coordinates": [-46.57421, -21.785741]
        }
    }

    return


def partner_get(request):
    request['id']
    return


def partner_search(request):
    request['lng']
    request['lat']
    return
