import queue
from typing import Any, Callable, Generator, List, Optional


class Node:
    @property
    def childs(self) -> List['Node']:
        raise NotImplementedError

    @property
    def parent(self) -> Optional['Node']:
        raise NotImplementedError

    @property
    def type(self):
        return self.__class__.__name__

    def __str__(self):
        return '<{}>'.format(self.type)

    def __repr__(self):
        return '<{}>'.format(self.type)


class AttrNode(Node):
    _attrs: List[str] = []

    @classmethod
    def attrs(cls):
        return cls._attrs

    def __getitem__(self, key):
        if not isinstance(key, str):
            raise ValueError
        if key not in self.attrs():
            raise AttributeError
        return getattr(self, key, None)

    def __repr__(self):
        return '<{type} {attrs}>'.format(
            type=self.type,
            attrs=', '.join(['{key}={value}'.format(key=key,
                                                    value=str(self[key]))
                             for key in self.attrs()]))


class SimpleNode(Node):
    def __init__(self, childs: List[Node], parent: Node = None):
        self._childs = childs
        self._parent = parent

    @property
    def childs(self):
        return self._childs

    @property
    def parent(self):
        return self._parent


class SimpleAttrNode(AttrNode):
    def __init__(self, childs: List[Node], parent: Node = None, **kwargs):
        self._childs = childs
        self._parent = parent
        for key, value in kwargs.items():
            setattr(self, key, value)

    @property
    def childs(self):
        return self._childs

    @property
    def parent(self):
        return self._parent


def dfs(node,
        visit: Optional[Callable[[Node], None]] = None,
        callback: Optional[Callable[[Node], None]] = None) -> Generator:
    '''Depth-first search'''

    if visit is not None:
        visit(node)

    yield node
    for child in node.childs:
        yield from dfs(child, visit)

    if callback is not None:
        callback(node)


def bfs(node,
        visit: Optional[Callable[[Node], None]] = None) -> Generator:
    '''Breadth-first search'''

    nodes_left: queue.Queue = queue.Queue()
    nodes_left.put(node)

    while not nodes_left.empty():
        node = nodes_left.get()
        yield node

        if visit is not None:
            visit(node)

        for child in node.childs:
            nodes_left.put(child)
