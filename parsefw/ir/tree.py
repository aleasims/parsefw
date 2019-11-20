"""This module provides abstract tree objects and manipulations."""

import queue
from typing import Callable, Generator, Optional, TypeVar, Union

from parsefw.utils.named_list import NamedList

TNode = TypeVar('TreeNodeMixin')


class TreeNodeMixin:
    @property
    def child_field_name(self):
        raise NotImplementedError

    @property
    def childs(self):
        return getattr(self, self.child_field_name)

    def add(self, node: TNode, position: Optional[int] = len(self.childs)):
        self.childs.insert(position, node)

    def remove(self, arg: Union[int, TNode]):
        if isinstance(arg, TreeNodeMixin):
            self.childs.pop(self.childs.index(arg))
        elif isinstance(arg, int):
            self.childs.pop(arg)

    def bfs(self):
        yield from bfs(self)

    def dfs(self):
        yield from dfs(self)


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
