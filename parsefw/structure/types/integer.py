from typing import Optional
from parsefw.structure.spectree import SpecNode, Byte, FieldOption
from parsefw.structure.types.byteseq import Byteseq
from parsefw.structure.attribute import IntAttr


class Int(Byteseq):
    def __init__(self, parent: Optional[SpecNode] = None, int_size: int = 4):
        """Default schema to specify a structure (format) is to specify:
            1. fields (childs)
            2. field options (edge modificators)
            3. new attributes with their expressions
            4. attributes relations (restrictions and etc.)
        """

        childs = [Byte(self)] * int_size
        modifs = [FieldOption.COM] * int_size
        new_attrs = {
            'int_value': IntAttr('Integer(./)')
        }
        super().__init__(parent, childs, modifs, **new_attrs)
