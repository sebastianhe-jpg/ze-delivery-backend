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
        app.app.testing = True
        self.app = app.app.test_client()

    @print_test_time_elapsed
    def test_home(self):
        result = self.app.get('/')
        assert result.status_code == 200


if __name__ == '__main__':
    unittest.main()