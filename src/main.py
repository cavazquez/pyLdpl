from src.parser import grammar
from src.build_python_code import Code
from src.tree import print_tree

def main():
    data = r"""
            data:
            n is number

            procedure:
            for n from 0 to 1000000 step 1 do
                display n lf
            repeat
            """
    #for toks,start,end in grammar.scan_string(data):
    #    print(toks, start, end)

    #print(grammar.search_string(data))

    code = Code()

    tree = grammar.parse_string(data)

    print_tree(tree, code)

    print(code.exporter())













if __name__ == "__main__":
    main()
