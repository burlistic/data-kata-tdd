# test_data_parser.py
import unittest
# from data_parser import DataParser
# from data_parser


class Test_TestDataParser(unittest.TestCase):

    # data_parser = DataParser()

    def test_missing_null(self):
        """Test for 'missing nulls'"""
        # result = data_parser.parse("\"test\",,\"test\"")
        result = DataParser.parse(""" "test","","test" """)
        expectedResult = ['\"test\"', '\"null\"', '\"test\"']
        # expectedResult = """ "test","null","test" """

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

    # data_parser.py


class DataParser:

    # def __init__(self, data):
    #     self.data = data

    def parse(input):
        # parsing logic
        parsedResult = []
        splitInput = input.split(",")

        for x in splitInput:
            if x == '""':
                x = '"null"'

            parsedResult.append(x.strip())

        return parsedResult


# if __name__ == "__main__":
#     sample_data = "apple,banana,cherry"
#     parser = DataParser(sample_data)
#     print(parser.parse())
