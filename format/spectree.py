from typing import Any, Callable, List, Optional

from format.runtime.types import FutureBool, FutureInt, FutureString
from format.tree import AttrNode, Node, SimpleAttrNode, SimpleNode, dfs, bfs


class Value(SimpleAttrNode):
    '''Represents raw byte sequence.

    Refers to words (terminal sequences).
    '''

    _attrs = ['length', 'endianness']

    def __init__(self, length: FutureInt, parent: Optional[Node] = None,
                 endianness: FutureString = 'big'):
        super().__init__([], parent,
                         length=length,
                         endianness=endianness)


class Type(SimpleAttrNode):
    '''Represents structured type.

    Refers to nonterminal symbol.
    '''

    _attrs = ['name']

    def __init__(self, name: str, struct: List[Node],
                 parent: Optional[Node] = None):
        super().__init__(struct, parent, name=name)


class OptionalType(Type):

    _attrs = ['name', 'condition']

    def __init__(self, name: str, struct: List[Node], condition: FutureBool,
                 parent: Optional[Node] = None):
        super().__init__(name, struct)
        self.condition = condition


class Select(SimpleNode):
    def __init__(self, variants: List[Node], parent: Optional[Node] = None):
        super().__init__(variants, parent)


class Repeat(SimpleNode):
    '''Represents repeated structure.

    Refers to recursion in grammars.
    '''

    pass


class RepeatCount(SimpleAttrNode, Repeat):
    '''Represents structure, repeated specified times.'''

    _attrs = ['count']

    def __init__(self, body: Node, count: FutureInt, parent: Optional[Node] = None):
        super().__init__([body], parent, count=count)


class RepeatUntil(Repeat):
    '''Represents structure, repeated until special symbol come across.'''

    def __init__(self, body: Node, delimiter: Value, parent: Optional[Node] = None):
        super().__init__([body, delimiter], parent)
