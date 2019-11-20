import unittest

from parsefw.structure.named_list import NamedList

"""Run tests
    This:
python -m unittest -vc tests.test_namedlist
    All:
python -m unittest discover -vcs tests
"""


class A:
    def __init__(self, label):
        self.label = label

    def __repr__(self):
        return '< {} >'.format(self.label)


class TestNamedList(unittest.TestCase):
    def setUp(self):
        self.nl = NamedList([A('a'), A('b'), A('c')])

    def test_init(self):
        NamedList([A('a'), A('b'), A('c')])
        NamedList()

    def test_len(self):
        self.assertEqual(len(self.nl), 3)

    def test_index(self):
        self.assertEqual(self.nl.index('a'), 0)

    def test_get(self):
        self.assertEqual(self.nl.get('b').label, 'b')
        self.assertEqual(self.nl.get(2).label, 'c')

    def test_insert_pop(self):
        self.nl.insert(2, A('e'))
        self.assertEqual(self.nl.pop(2).label, 'e')

    def test_append_pop(self):
        self.nl.append(A('e'))
        self.assertEqual(len(self.nl), 4)
        self.nl.pop('e')

    def test_labels(self):
        self.assertEqual(self.nl.labels(), ['a', 'b', 'c'])

    def test_getitem(self):
        self.assertEqual(self.nl['b'].label, 'b')
        self.assertEqual(self.nl[2].label, 'c')

    def test_setitem_get(self):
        self.nl[2] = A('e')
        self.assertEqual(self.nl.get(2).label, 'e')
        self.nl[2] = A('c')
        self.assertEqual(self.nl.get('c').label, 'c')


if __name__ == '__main__':
    unittest.main()
