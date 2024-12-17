# test_data_parser.py

import unittest

# append not working ???
# import sys
# sys.path.append("code")


from code.data_parser1 import DataParser

# from data_parser

class Test_TestDataParser(unittest.TestCase):

    # data_parser = DataParser()

    def test_missing_null(self):
        """Test for 'missing nulls'"""
        result = DataParser.parse(self, """ "test","","test" """)
        expectedResult = ['\"test\"', '\"null\"', '\"test\"']

        self.assertEqual(result, expectedResult)

# tests

# missing nulls
# input = "test", , "test"
# expected output = "test", null, "test"

# missing fields
# input = "test", "test"
# expected output = "test", null, "test"

# casing
# booleans incorrect
# duplicate records

# Makes the test module executable


if __name__ == "__main__":
    unittest.main()
    # unittest.main(verbosity=2)
