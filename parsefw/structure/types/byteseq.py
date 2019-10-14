from typing import Optional
from parsefw.structure.spectree import SpecNode, Byte, FieldOption


class Byteseq(SpecNode):
    def __init__(self, parent: Optional[SpecNode] = None,
                 length: Optional[int] = None):
        """Default schema to specify a structure (format) is to specify:
            1. fields (childs)
            2. field options (edge modificators)
            3. new attributes with their expressions
            4. attributes relations (restrictions and etc.)
        """

        childs = [Byte(self)] * length
        modifs = [FieldOption.COM] * length
        super().__init__(parent, childs, modifs)
