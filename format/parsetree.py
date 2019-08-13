from typing import List, Optional

from format.spectree import SpecNode
from format.tree import AttrNode, SimpleAttrNode


class ParseNode(SimpleAttrNode):
    _attrs = ['name', 'start', 'end']

    def __init__(self, start: int, end: int,
                 childs: List['ParseNode'],
                 parent: Optional['ParseNode'] = None,
                 **kwargs):
        super().__init__(childs, parent, start=start, end=end, **kwargs)


class Struct(ParseNode):
    pass


class Array(ParseNode):
    _attrs = ParseNode._attrs + ['count']

    def __init__(self, start: int, end: int, count: int,
                 childs: List['ParseNode'],
                 parent: Optional['ParseNode'] = None):
        super().__init__(start, end, childs, parent, count=count)        


class Value(ParseNode):
    def __init__(self, start: int, end: int,
                 parent: Optional['ParseNode'] = None):
        super().__init__(start, end, [], parent)
