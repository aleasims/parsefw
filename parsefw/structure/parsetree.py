from parsefw.structure.tree import Node


class ParseNode(Node):
    def __init__(self, start, end, label, *args, **kwargs):
        super().__init__(*args, **kwargs, start=start, end=end, label=label)
        self.fields = self.childs


class Struct(ParseNode):
    pass


class Array(ParseNode):
    def __init__(self, start, end,
                 parent=None, childs=None, label=None,
                 **kwargs):
        super().__init__(parent, childs, label, start=start, end=end, **kwargs)


class Value(ParseNode):
    pass
