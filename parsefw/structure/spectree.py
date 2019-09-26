from typing import Any, Callable, List, Optional

from parsefw.structure.runtime.types import FutureBool, FutureInt, FutureString
from parsefw.structure.tree import AttrNode, Node, SimpleAttrNode, SimpleNode, bfs, dfs


class SpecNode(AttrNode):
    _attrs = ['name', 'offset']


class Value(SimpleAttrNode, SpecNode):
    '''Represents raw byte sequence.

    Refers to words (terminal sequences).
    '''

    _attrs = SpecNode._attrs + ['length', 'endianness']

    def __init__(self, length: FutureInt, parent: Optional[Node] = None,
                 endianness: FutureString = 'big'):
        super().__init__([], parent,
                         length=length,
                         endianness=endianness)


class Type(SimpleAttrNode, SpecNode):
    '''Represents structured type.

    Refers to nonterminal symbol.
    '''

    def __init__(self, name: str, struct: List[Node],
                 parent: Optional[Node] = None):
        super().__init__(struct, parent, name=name)


class OptionalType(Type):

    _attrs = Type._attrs + ['condition']

    def __init__(self, name: str, struct: List[Node], condition: FutureBool,
                 parent: Optional[Node] = None):
        super().__init__(name, struct)
        self.condition = condition


class Select(SimpleNode, SpecNode):
    def __init__(self, variants: List[Node], parent: Optional[Node] = None):
        super().__init__(variants, parent)


class Repeat(SpecNode):
    '''Represents repeated structure.

    Refers to recursion in grammars.
    '''

    pass


class RepeatCount(SimpleAttrNode, Repeat):
    '''Represents structure, repeated specified times.'''

    _attrs = Repeat._attrs + ['count']

    def __init__(self, body: Node, count: FutureInt, parent: Optional[Node] = None):
        super().__init__([body], parent, count=count)


class RepeatUntil(Repeat):
    '''Represents structure, repeated until special symbol come across.'''

    def __init__(self, body: Node, delimiter: Value, parent: Optional[Node] = None):
        super().__init__([body, delimiter], parent)
