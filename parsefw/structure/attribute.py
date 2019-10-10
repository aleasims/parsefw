from enum import Enum


class AttributeType(Enum):
    INT = 0
    BOOL = 1
    STR = 2
    BYTES = 3


class Attribute:
    """Represent tree node atribute."""

    def __init__(self, _type: AttributeType, expression: str):
        self.type = _type
        self.expression = expression

    @property
    def value(self):
        raise RuntimeError('Can not be evaluated')
