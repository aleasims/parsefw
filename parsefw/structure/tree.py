"""This module provides abstract tree objects and manipulations."""

import queue
from typing import Callable, Generator, List, Optional, TypeVar, Union

TNode = TypeVar('Node')


class Node:
    """Tree node."""

    def __init__(self, childs: Optional[List[TNode]] = None,
                 parent: Optional[TNode] = None,
                 label: Optional[str] = None):
        self.childs = childs if childs is not None else []
        self.parent = parent
        self.label = label if label is not None else 'node_{}'.format(id(self))

    def add_child(self, node: TNode, position: Optional[int] = None):
        position = len(self.childs) if position is None else position
        self.childs.insert(position, node)

    def remove_child(self, arg: Union[int, TNode]):
        if isinstance(arg, Node):
            self.childs.pop(self.childs.index(arg))
        elif isinstance(arg, int):
            self.childs.pop(arg)

    def bfs(self):
        yield from bfs(self)

    def dfs(self):
        yield from dfs(self)

    def __str__(self):
        return '<{type} {label}>'.format(
            type=self.__class__.__name__,
            label=self.label)

    def __repr__(self):
        return '<{type} {label}>'.format(
            type=self.__class__.__name__,
            label=self.label)


class AttrNode(Node):
    """Attribute tree node."""

    def __init__(self, childs=None, parent=None, label=None, **kwargs):
        super().__init__(childs, parent, label)
        self.attrs = kwargs

    def get_attr(self, name):
        return self.attrs[name]

    def set_attr(self, name, value):
        self.attrs[name] = value

    def __getitem__(self, key):
        return self.get_attr(key)

    def __setitem__(self, key, value):
        self.set_attr(key, value)

    def __repr__(self):
        return '<{type} {label} [{attrs}]>'.format(
            type=self.__class__.__name__,
            label=self.label,
            attrs=', '.join([str(key) for key in self.attrs.keys()]))


def dfs(node,
        visit: Optional[Callable[[TNode], None]] = None,
        callback: Optional[Callable[[TNode], None]] = None) -> Generator:
    """Depth-first search."""

    if visit is not None:
        visit(node)

    yield node
    for child in node.childs:
        yield from dfs(child, visit)

    if callback is not None:
        callback(node)


def bfs(node,
        visit: Optional[Callable[[TNode], None]] = None) -> Generator:
    """Breadth-first search."""

    nodes_left: queue.Queue = queue.Queue()
    nodes_left.put(node)

    while not nodes_left.empty():
        node = nodes_left.get()
        yield node

        if visit is not None:
            visit(node)

        for child in node.childs:
            nodes_left.put(child)
