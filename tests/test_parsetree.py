import unittest

from parsefw.structure.parsetree import Array, Struct, Value

# python -m unittest discover -s tests -vc


class TestParseTree(unittest.TestCase):
    def test_creation(self):
        n1 = Value(1, 10)
        n2 = Value(10, 12)
        n3 = Struct(1, 12, [n1, n2])
        n4, n5, n6 = Value(12, 13), Value(13, 14), Value(14, 15)
        n6 = Array(12, 15, [n4, n5, n6])
        n7 = Struct(1, 15, [n3, n6])

    def test_bfs(self):
        n1 = Value(1, 10)
        n2 = Value(10, 12)
        n3 = Struct(1, 12, [n1, n2])
        n4, n5, n6 = Value(12, 13), Value(13, 14), Value(14, 15)
        n6 = Array(12, 15, [n4, n5, n6])
        n7 = Struct(1, 15, [n3, n6])
        [i for i in n7.bfs()]

    def test_dfs(self):
        n1 = Value(1, 10)
        n2 = Value(10, 12)
        n3 = Struct(1, 12, [n1, n2])
        n4, n5, n6 = Value(12, 13), Value(13, 14), Value(14, 15)
        n6 = Array(12, 15, [n4, n5, n6])
        n7 = Struct(1, 15, [n3, n6])
        [i for i in n7.dfs()]


if __name__ == '__main__':
    unittest.main()
