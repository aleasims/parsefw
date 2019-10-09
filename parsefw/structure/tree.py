"""This module provides abstract tree objects and manipulations."""

import queue
from typing import Callable, Generator, List, Optional, TypeVar, Union

TNode = TypeVar('Node')


class Node:
    """Attribute tree node.

    Attributes:
        parent (Node) - parent node
        childs (List[Node]) - list of child nodes
    """

    def __init__(self,
                 parent: Optional[TNode] = None,
                 childs: Optional[List[TNode]] = None,
                 **kwargs):
        self.childs = childs if childs is not None else []
        self.parent = parent
        self.attrs = list(kwargs.keys())
        for key, value in kwargs.items():
            setattr(self, key, value)

    def classname(self):
        return self.__class__.__name__

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
        return '{type}'.format(
            type=self.classname())

    def __repr__(self):
        return '<{type} {attrs}>'.format(
            type=self.classname(),
            attrs=self.attrs)


class Tree(Node):
    """Represents root node."""

    def __init__(self, childs=None, label=None, **kwargs):
        super().__init__(None, childs, label, **kwargs)


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
