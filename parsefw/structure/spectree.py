from parsefw.structure.regtree import RegNode, EdgeModifier


FieldOption = EdgeModifier


class SpecNode(RegNode):
    """Represent node as a node of spectree."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields = self.childs

    def add_field(self, *args, **kwargs):
        return self.add_child(*args, **kwargs)


class Struct(SpecNode):
    pass


class Byte(SpecNode):
    def __init__(self, parent: SpecNode):
        super().__init__(parent)

    def add_field(self, *args, **kwargs):
        raise TypeError('Only <Struct> can have fields')


if __name__ == "__main__":
    root = Struct()
    print([name for name in dir(root) if not name.startswith('__')])
    b = Byte(root)
    print('')
    print([name for name in dir(b) if not name.startswith('__')])
    print('done')
