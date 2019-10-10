from enum import Enum
from typing import List, Optional

from parsefw.structure.tree import Node


class EdgeModifier(Enum):
    COM = 0  # <no modifier>
    REP = 1  # *
    OPT = 2  # ?


class RegNode(Node):
    def __init__(self,
                 parent: Optional[Node] = None,
                 childs: Optional[List[Node]] = None,
                 modifs: Optional[List[EdgeModifier]] = None,
                 **kwargs):
        super().__init__(parent, childs, **kwargs)
        self.modifs = modifs if modifs is not None else []
        assert len(self.childs) == len(
            self.modifs), 'All childs must be marked'
