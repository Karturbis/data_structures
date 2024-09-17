class Binary_Node:
    def __init__(self, name: str, value = None):
        self.name = name
        self.value = value
        self.left = None
        self.right = None

class Binary_Tree:
    def __init__(self):
        self.root = Binary_Node("root")

    def search_bin_tree(self, key):
        