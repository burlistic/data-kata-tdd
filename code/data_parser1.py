class DataParser:

    def __init__(self, data):
        self.data = data

    def parse(self, stringinput):
        # parsing logic
        parsedResult = []
        splitInput = stringinput.split(",")

        for x in splitInput:
            if x == '""':
                x = '"null"'

            parsedResult.append(x.strip())

        return parsedResult

# if __name__ == "__main__":
#     sample_data = "apple,banana,cherry"
#     parser = DataParser(sample_data)
#     print(parser.parse())
