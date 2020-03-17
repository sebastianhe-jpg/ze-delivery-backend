# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
unit test to check if flask is running properly on server
"""
import unittest
from .utils import print_test_time_elapsed
import app

class MyTestCase(unittest.TestCase):
    def setUp(self):
        app.APP.testing = True
        self.app = app.APP.test_client()

    @print_test_time_elapsed
    def test_home(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()