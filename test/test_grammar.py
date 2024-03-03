import unittest

from src.parser import grammar

class TestMain(unittest.TestCase):

    def test_hello_world(self):
        data = r"""
            procedure:
            display  "
            """
        tree = grammar.parse(data)
        print(tree)
        self.assertEqual("", tree)

#display "Hello World!" crlf

