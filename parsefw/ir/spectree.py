from parsefw.ir.tree import TreeNodeMixin
from parsefw.utils.named_list import NamedList


class Struct(TreeNodeMixin):
    def __init__(self, fields: NamedList[tuple(Struct, Expression, Address)],
                 attrs: dict):
        self.field = fields
        self.attrs = attrs

    @property
    def child_field_name(self):
        raise 'fields'
