import unittest

from src.parser import grammar
from src.build_python_code import Code
from src.tree import print_tree

class TestMain(unittest.TestCase):

    @unittest.skip("WIP")
    def test_hello_world(self):
        data = r"""
            procedure:
            display "Hello World" crlf
            """
        tree = grammar.parse_string(data)
        code = Code()
        print_tree(tree, code)

        res = """def main():
        print("Hello World")
            """

        print(res)
        print(code.exporter())

        self.assertEqual(code.exporter(), res)
