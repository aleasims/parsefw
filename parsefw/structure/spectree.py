
import sys
sys.path.insert(0, '/home/alea/parsefw')

from parsefw.structure.regtree import RegNode


class SpecNode(RegNode):
    """Marks that node as a node of spectree."""

    pass


class Struct(SpecNode):
    pass


class Byte(SpecNode):
    def __init__(self, parent: SpecNode):
        super().__init__(parent)


if __name__ == "__main__":
    root = Struct()
    b = Byte(root)
