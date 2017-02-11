# unittest_doc.py

from testing_doc import * # import all methods from testing_doc file
import unittest           # import the testing module

class TestInterest(unittest.TestCase):  # the TestInterest class inherits from unittest.TestCase class
    def test_simple_interest(self):
        self.assertEqual(simple_interest(500, 5, 2), 50.0)

    def test_fv_compound_interest(self):
        self.assertEqual(fv_compound_interest(500, 5, 2), 550)

unittest.main()