import os
import sys

script_path = os.path.realpath(__file__)
tests_dir = os.path.dirname(script_path)
root_dir = os.path.dirname(tests_dir)
sys.path.insert(0, root_dir)


def test_spectree():
    from format.spectree import Type, Value, RepeatCount, RepeatUntil, Select, OptionalType, dfs, bfs
    from format.runtime.types import FutureBool, FutureInt

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

    print('DFS:')
    for i in dfs(t6):
        print(repr(i))

    print('\nBFS:')
    for i in bfs(t6):
        print(repr(i))

    print('OK')


if __name__ == "__main__":
    test_spectree()
