"""Module providing data parsing methods"""


class DataParser:
    """Data Parsers class - file named data_parser1.py to avoid import issues"""

    def __init__(self, data):
        self.data = data

    def parse(self, param : str, stringinput : str):
        """ Parse Method"""

        # params

            # l = lower,
            # c = caps,
            # n = add in nulls for missing items,
            # b = format booleans,
            # d = remove duplicates


        # parsing logic
        parsed_result = []

        if param == "l":
            stringinput = stringinput.lower()

        split_input = stringinput.split(",")

        for x in split_input:
            if x == '""':
                x = '"null"'

            parsed_result.append(x.strip())

        return parsed_result

# if __name__ == "__main__":
#     sample_data = "apple,banana,cherry"
#     parser = DataParser(sample_data)
#     print(parser.parse())
