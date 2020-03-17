# -*- coding: utf-8 -*-
# !/usr/bin/env python3
import unittest
from .utils import print_test_time_elapsed
from views import partners_view
"""
unit test module for modules in views folder
"""

class TestViews(unittest.TestCase):
    def setUp(self):
        self.partners_data = [
            {
            "id": 3,
            "coverageArea":{
                "coordinates": [
                    [[[-38.6577, -3.7753],
                      [-38.63212, -3.81418],
                      [-38.61925, -3.82873],
                      [-38.59762, -3.84004],
                      [-38.58727, -3.84345],
                      [-38.58189, -3.8442],
                      [-38.57667, -3.84573],
                      [-38.56706, -3.85015],
                      [-38.56637, -3.84937],
                      [-38.56268, -3.84286],
                      [-38.56148, -3.83772],
                      [-38.55881, -3.82411],
                      [-38.55577, -3.81507],
                      [-38.62577, -3.7472],
                      [-38.63332, -3.7496],
                      [-38.65049, -3.76057],
                      [-38.6577, -3.7753]]]
                ]
            }
        },
            {
            "id": 1,
            "coverageArea": {
                "type": "MultiPolygon",
                "coordinates": [
                    [[[30, 20], [45, 40], [10, 40], [30, 20]]],
                    [[[15, 5], [40, 10], [10, 20], [5, 10], [15, 5]]]
                ]
            }
        }
        ]

    def tearDown(self):
        pass

    @print_test_time_elapsed
    def test_view_closest_partner(self):
        """
        Tests summaries using the simplest algorithm
        """
        input_lng = -46.57421
        input_lat = -21.785741
        partners_data = self.partners_data
        nearest_partner = partners_view.find_closest_partner(input_lng, input_lat, partners_data)

        self.assertIsInstance(nearest_partner, dict)
        self.assertEqual(nearest_partner['id'],3)


if __name__ == '__main__':
    unittest.main()
