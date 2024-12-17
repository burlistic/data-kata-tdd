"""Tests"""

import unittest

# append not working ???
# import sys
# sys.path.append("code")


from code.data_parser1 import DataParser

# from data_parser

class TestDataParser(unittest.TestCase):
    """Test Class"""

    # todo - see if there is a cleaner way to pass in the strings

    # missing nulls
    # input = "test", , "test"
    # expected output = "test", null, "test"

    # todo - see if Pythong supports options params and implement

    def test_missing_null(self):
        """Test for 'missing nulls'"""
        result = DataParser.parse(self, "", """ "test","","test" """)
        expected_result = ['\"test\"', '\"null\"', '\"test\"']

        self.assertEqual(result, expected_result)


    def test_fixed_casing_to_lower(self):
        """Test for 'missing nulls'"""
        result = DataParser.parse(self,"l" , """ "Test","tEst","TeST" """)
        expected_result = ['\"test\"', '\"test\"', '\"test\"']

        self.assertEqual(result, expected_result)

# booleans incorrect
# duplicate records

# Makes the test module executable


if __name__ == "__main__":
    unittest.main()
    # unittest.main(verbosity=2)
