"""This module provides abstract tree objects and manipulations."""

import queue
from typing import Callable, Generator, Optional, TypeVar, Union
from parsefw.structure.named_list import NamedList

TNode = TypeVar('Node')


class Node:
    """Attribute tree node.

    Attributes:
        label (str, optional)
        parent (Node, optional)
        childs (NamedList, optional)
    """

    def __init__(self, label=None):
        self.label = label
        self.childs = None
        self._parent = None

    @classmethod
    def new(cls, label=None, parent=None, childs=None):
        node = cls(label)
        node.parent = parent
        node.childs = childs
        return node

    def classname(self):
        return self.__class__.__name__

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        if not isinstance(value, Node):
            raise TypeError
        self._parent = value

    def add_child(self, node: TNode, position: Optional[int] = None):
        if self.childs is None:
            self.childs = NamedList(keyattr='label')
        position = position if position is not None else len(self.childs)
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
        return self.classname()

    def __repr__(self):
        return '<{type} {attrs}>'.format(
            type=self.classname(),
            attrs=self.attrs)


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
