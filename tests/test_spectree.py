import unittest
from format.spectree import Type, Value, RepeatCount, RepeatUntil, Select, OptionalType, dfs, bfs
from format.runtime.types import FutureBool, FutureInt

class TestSpecTree(unittest.TestCase):
    def test_creation(self):
        t1 = Type('mytype', [Value(FutureInt('1')), Value(FutureInt('3'))])
        t2 = RepeatCount(t1, FutureInt('3'))
        t3 = OptionalType('opttype', [Value(FutureInt('4'))], FutureBool('true'))
        t4 = Select([t3, t1])
        t5 = Type('magic', [Value(FutureInt('2'))])
        t6 = Type('big', [t5, t2, t4])

    def test_inheritance(self):
        class Int(Type):
            def __init__(self):
                val = Value(FutureInt('4'))
                super().__init__('Int', [val])
        t1 = Type('mytype', [Value(FutureInt('1')), Value(FutureInt('3'))])
        t2 = RepeatCount(t1, FutureInt('3'))
        t3 = OptionalType('opttype', [Int()], FutureBool('true'))
        t4 = Select([t3, t1])
        t5 = Type('magic', [Value(FutureInt('2'))])
        t6 = Type('big', [t5, t2, t4])

    def test_bfs(self):
        class Int(Type):
            def __init__(self):
                val = Value(FutureInt('4'))
                super().__init__('Int', [val])
        t1 = Type('mytype', [Value(FutureInt('1')), Value(FutureInt('3'))])
        t2 = RepeatCount(t1, FutureInt('3'))
        t3 = OptionalType('opttype', [Int()], FutureBool('true'))
        t4 = Select([t3, t1])
        t5 = Type('magic', [Value(FutureInt('2'))])
        t6 = Type('big', [t5, t2, t4])
        result = [i for i in bfs(t6)]

    def test_dfs(self):
        class Int(Type):
            def __init__(self):
                val = Value(FutureInt('4'))
                super().__init__('Int', [val])
        t1 = Type('mytype', [Value(FutureInt('1')), Value(FutureInt('3'))])
        t2 = RepeatCount(t1, FutureInt('3'))
        t3 = OptionalType('opttype', [Int()], FutureBool('true'))
        t4 = Select([t3, t1])
        t5 = Type('magic', [Value(FutureInt('2'))])
        t6 = Type('big', [t5, t2, t4])
        result = [i for i in dfs(t6)]


if __name__ == "__main__":
    unittest.main()
