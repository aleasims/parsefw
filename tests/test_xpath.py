import unittest

from parsefw.structure.xpath import Path

"""Run tests
    This:
python -m unittest -vc tests.test_xpath
    All:
python -m unittest discover -vcs tests
"""


class TestTree(unittest.TestCase):
    def test_tokenizer(self):
        path = Path('abc')
        #print(list(path.tokenize('/abc/cde//fem@1223')))


if __name__ == '__main__':
    unittest.main()
