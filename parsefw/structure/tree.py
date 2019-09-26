"""This module provides abstract tree objects and manipulations."""

import queue
from typing import Any, Callable, Generator, List, Optional, TypeVar

TNode = TypeVar('Node')


class Node:
    """Tree node interface."""

    childs: List[TNode] = []
    parent: Optional[TNode] = None

    def __init__(self, childs, parent=None):
        self.childs = childs
        self.parent = parent

    def add_child(self, node: TNode, position: Optional[int]):
        if position is not None and position not in range(0, len(self.childs) + 1):
            raise ValueError(
                'position argument must be in range [0 ... len(childs)]')
        pos = len(self.childs) if position is None else position
        self.childs.insert(pos, node)
        node.parent = self

    def remove_child(self, node: Optional[TNode] = None,
                     position: Optional[int] = None):
        if node is not None:
            

    @property
    def type(self):
        return self.__class__.__name__

    def __str__(self):
        return '<{}>'.format(self.type)

    def __repr__(self):
        return '<{}>'.format(self.type)

    def bfs(self):
        yield from bfs(self)

    def dfs(self):
        yield from dfs(self)


class AttrNode(Node):
    """Attribute tree node interface."""

    _attrs: List[str] = []

    @classmethod
    def attrs(cls):
        return cls._attrs

    def __getitem__(self, key):
        if not isinstance(key, str):
            raise ValueError(key)
        if key not in self.attrs():
            raise AttributeError(key)
        return getattr(self, key, None)

    def __repr__(self):
        return '<{type} {attrs}>'.format(
            type=self.type,
            attrs=', '.join(['{key}={value}'.format(key=key,
                                                    value=str(self[key]))
                             for key in self.attrs()]))


class SimpleNode(Node):
    """Simple implementation of init."""

    def __init__(self, childs: List[TNode], parent: TNode):
        self._childs = childs
        self._parent = parent

    @property
    def childs(self):
        return self._childs

    @property
    def parent(self):
        return self._parent


class SimpleAttrNode(SimpleNode, AttrNode):
    def __init__(self, childs: List[TNode], parent: TNode, **kwargs):
        super().__init__(childs, parent)
        for key, value in kwargs.items():
            setattr(self, key, value)


def dfs(node,
        visit: Optional[Callable[[TNode], None]] = None,
        callback: Optional[Callable[[TNode], None]] = None) -> Generator:
    '''Depth-first search'''

    if visit is not None:
        visit(node)

    yield node
    for child in node.childs:
        yield from dfs(child, visit)

    if callback is not None:
        callback(node)


def bfs(node,
        visit: Optional[Callable[[TNode], None]] = None) -> Generator:
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
