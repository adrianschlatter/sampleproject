# -*- coding: utf-8 -*-
"""
Unit test example

All files in this directory named "test_*.py" are automatically identified
as unittests by 'python setup.py test'.
"""

import unittest
import myPackage  # import code to be tested here (add to your python path!)


class Test_Something(unittest.TestCase):
    """Test something. All methods in this class named 'test_XXX' are assumed
    to be tests."""

    def setUp(self):
        """Code that will be run before each test in this class"""
        pass

    def test_one(self):
        """1st test"""

        # add here test code
        self.assertTrue(True)

    def test_two(self):
        """2nd test"""

        # add here test code
        self.assertTrue(True)


if __name__ == '__main__':
    # This enables running the unit tests by running this script which is
    # much more convenient than 'python setup.py test' while developing tests.
    unittest.main()
