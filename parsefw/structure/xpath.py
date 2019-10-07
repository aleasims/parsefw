from io import StringIO

SPECIAL_SYMBOLS = set('/@')


class Path:
    def __init__(self, string):
        self.string = string
        self.parse()

    def parse(self):
        """Syntax:
        / - refers to selecting child
        @ - refers to selecting attribute
        """

        string = self.string
        tokens = self.tokenize(string)

    @staticmethod
    def tokenize(string):
        stream = StringIO(string)
        buffer = ''

        while True:
            symbol = stream.read(1)
            if not symbol:
                yield buffer
                break

            if symbol in SPECIAL_SYMBOLS:
                yield buffer
                yield symbol
                buffer = ''
            else:
                buffer = buffer + symbol
