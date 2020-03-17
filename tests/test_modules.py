# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
unit test module for modules in mods folder
"""
import unittest
from mods import sanitize_input_module
from mods import input_validator_module
from mods import formatting_module
from mods import partners
from .utils import print_test_time_elapsed


class TestModules(unittest.TestCase):
    """
    module class for unit test
    """
    def setUp(self):
        class TestClass:
            """
            class to mime request.json input
            """
            json = {
                "string": "str",
                "integer": 123,
                "double": 1.15,
                "array": ["hi"],
                "dict": {"hey":"ho lets go"},
                "bool": True
            }
        self.test_class = TestClass

        self.lng = -46.57421
        self.lat = -21.785741
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
            }, {
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
    def test_module_sanizite_input(self):
        """
        test sanitize_input_module
        """
        input_string = "hey"
        input_script = "<script> alert() </script> testing"
        clean_input1 = sanitize_input_module.entry_clean(input_string)
        clean_input2 = sanitize_input_module.entry_clean(input_script)
        self.assertEquals(input_string, clean_input1)
        self.assertNotEquals(input_script, clean_input2)

    @print_test_time_elapsed
    def test_module_input_validator(self):
        """
        test validate key module
        """
        input_request = self.test_class
        invalid, reason = input_validator_module.validate_keys(input_request,
                                                               ["string"],
                                                               {"string": str, "integer": int})
        self.assertIs(invalid, False)
        self.assertIs(reason, None)

    @print_test_time_elapsed
    def test_module_formatting(self):
        """
        Tests output formate module
        """
        input_text = "output text"
        input_data = {"data": "to show"}
        output_text = formatting_module.output_format(input_text, input_data)
        self.failUnlessEqual(output_text['message'], input_text)
        self.failUnlessEqual(output_text['data'], "to show")

    @print_test_time_elapsed
    def test_view_closest_partner(self):
        """
        Tests find closest function from partners class
        """
        partner = partners.Partner(lng=self.lng, lat=self.lat)
        closest = partner.partner_find_closest(self.partners_data) if self.partners_data else None
        self.assertIsInstance(closest, dict)
        self.assertIsInstance(closest['id'], int)


if __name__ == '__main__':
    unittest.main()
