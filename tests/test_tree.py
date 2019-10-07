import unittest

from parsefw.structure.tree import Node, dfs, bfs

"""Run tests
    This:
python -m unittest -vc tests.test_tree
    All:
python -m unittest discover -vcs tests
"""


class TestTree(unittest.TestCase):
    def test_tree_build(self):
        """Build tree
                n1
              /   |
            n2    n3
           /  |
        n4    n5
        """

        nodes = [Node(label='n{}'.format(i + 1)) for i in range(5)]
        nodes[0].add_child(nodes[1])
        nodes[0].add_child(nodes[2])
        nodes[1].add_child(nodes[3])
        nodes[1].add_child(nodes[4])

    def test_dfs(self):
        """Dfs tree
                n1
              /   |
            n2    n3
           /  |
        n4    n5
        """

        nodes = [Node(label='n{}'.format(i + 1)) for i in range(5)]
        nodes[0].add_child(nodes[1])
        nodes[0].add_child(nodes[2])
        nodes[1].add_child(nodes[3])
        nodes[1].add_child(nodes[4])
        list(dfs(nodes[0]))

    def test_bfs(self):
        """Bfs tree
                n1
              /   |
            n2    n3
           /  |
        n4    n5
        """

        nodes = [Node(label='n{}'.format(i + 1)) for i in range(5)]
        nodes[0].add_child(nodes[1])
        nodes[0].add_child(nodes[2])
        nodes[1].add_child(nodes[3])
        nodes[1].add_child(nodes[4])
        list(bfs(nodes[0]))


if __name__ == '__main__':
    unittest.main()
