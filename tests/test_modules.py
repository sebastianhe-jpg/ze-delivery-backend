# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
unit test module for modules in mods folder
"""
import unittest
from .utils import print_test_time_elapsed
from mods import sanitize_input_module
from mods import input_validator_module
from mods import formatting_module


class TestModules(unittest.TestCase):
    def setUp(self):
        class TestClass:
            json = {
                "string": "str",
                "integer": 123,
                "double": 1.15,
                "array": ["hi"],
                "dict": {"hey":"ho lets go"},
                "bool": True
            }
        self.testClass = TestClass

    def tearDown(self):
        pass

    @print_test_time_elapsed
    def test_module_sanizite_input(self):
        """
        Tests summaries using the simplest algorithm
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
        Tests summaries using the simplest algorithm
        """
        input_request = self.testClass
        invalid, reason = input_validator_module.validate_keys(input_request, ["string"], {"string": str, "integer": int})
        self.assertIs(invalid, False)
        self.assertIs(reason, None)

    @print_test_time_elapsed
    def test_module_formatting(self):
        """
        Tests summaries using the simplest algorithm
        """
        input_text = "output text"
        input_data = {"data": "to show"}
        output_text = formatting_module.output_format(input_text, input_data)
        self.assertEqual(output_text['message'], input_text)
        self.assertEqual(output_text['data'], "to show")


if __name__ == '__main__':
    unittest.main()
