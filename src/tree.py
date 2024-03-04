
def print_tree(tree, code, indent=0):
    for item in tree:
        if isinstance(item, list):
            print_tree(item, indent + 1)
        if item[0] == "display":
            end = """"\\n" """
            if item[2] == "crlf":
                end = """"\\r\\n" """
            else:
                raise "control error"
            code.add_print(item[1], end)
        else:
            print("  " * indent + str(item))
