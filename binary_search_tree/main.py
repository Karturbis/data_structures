class DuplicateKeyError(Exception):
    """Exception raised, when an already
    existing key is inserted into a tree."""


class KeyNotFoundError(Exception):
    pass


class Binary_Node:
    def __init__(self, key: str, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class Binary_Search_Tree:

    def __init__(self, root_key, root_val=None):
        self.root = Binary_Node(root_key, root_val)
        self.root.left = Binary_Node("Caspian", "18")
        self.root.left.left = Binary_Node("Ahlfeld", "80")

    def insert_node(self, key, value):
        if key:
            self._insert_node_inner(str(key), value, self.root)
        else:
            raise ValueError

    def _insert_node_inner(self, key, value, position):
        if position:
            if key == position.key:
                raise DuplicateKeyError
            elif key < position.key:
                self._insert_node_inner(key, value, position.left)
            elif key > position.key:
                self._insert_node_inner(key, value, position.right)
        else:
            position = Binary_Node(key, value)

    def delete_node(self, key):
        pass

    def get_value(self, key: str, position = None):
        if not position:
            position = self.root
        if key:
            value = self._get_value_inner(str(key), position)
            if value:
                return value
            print("Key not found")
        else:
            raise ValueError

    def _get_value_inner(self, search_key: str, position: Binary_Node):
        if not position:
            raise KeyNotFoundError
        elif search_key == position.key:
            return position
        elif search_key < position.key:
            self._get_value_inner(search_key, position.left)
        elif search_key > position.key:
            self._get_value_inner(search_key, position.right)
        


if __name__ == "__main__":
    bin_tree = Binary_Search_Tree("root")
    print(bin_tree.get_value("Ahlfeld"))
