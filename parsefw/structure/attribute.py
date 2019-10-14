class Attribute:
    """Represent tree node atribute."""

    def __init__(self, expression: str):
        self.expression = expression


class IntAttr(Attribute):
    pass


class BoolAttr(Attribute):
    pass


class StrAttr(Attribute):
    pass


class BytesAttr(Attribute):
    pass
