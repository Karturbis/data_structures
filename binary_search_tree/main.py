class DuplicateKeyError(Exception):
    """Exception raised, when an already
    existing key is inserted into a tree."""


class KeyNotFoundError(Exception):
    pass


class Binary_Node:
    def __init__(self, key: str, parent, value=None):
        self.parent = parent
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class Binary_Search_Tree:

    def __init__(self, root_key, root_val=None):
        self.root = Binary_Node(root_key, None, root_val)

    def insert_node(self, key, value):
        if key:
            self._insert_node_inner(str(key), value, self.root)
        else:
            raise ValueError

    def _insert_node_inner(self, key, value, position):
        if position:
            if key < position.key:
                if position.left:
                    if position.left.key == key:
                        raise DuplicateKeyError
                    self._insert_node_inner(key, value, position.left)
                else:
                    position.left = Binary_Node(key, value)
            else:
                if position.right:
                    if position.right.key == key:
                        raise DuplicateKeyError
                    self._insert_node_inner(key, value, position.right)
                else:
                    position.right = Binary_Node(key, value)
        else:
            position = Binary_Node(key, value)

    def delete_node(self, key:str):
        if key:
            self._delete_node_inner(str(key), self.root)
        else:
            raise ValueError

    def _delete_node_inner(self, key, position):
        if key < position.key:
            self._delete_node_inner(key, position.left)
        else:
            if position.left:
                if position.right:
                    # IMPLEMENT mininhalt
                else:

    def get_value(self, key: str, position=None):
        return self.get_node(key, position).value

    def get_node(self, key: str, position=None):
        if not position:
            position = self.root
        if key:
            node = self._get_node_inner(str(key), position)
            if node:
                return node
            print("Key not found")
        else:
            raise ValueError

    def _get_node_inner(self, search_key: str, position: Binary_Node):
        if not position:
            raise KeyNotFoundError
        elif search_key == position.key:
            return position
        elif search_key < position.key:
            return self._get_node_inner(search_key, position.left)
        elif search_key > position.key:
            return self._get_node_inner(search_key, position.right)


if __name__ == "__main__":
    bin_tree = Binary_Search_Tree("root")
    while True:
        user_input = input("Commands:\nadd node: an\nget value: gv\n>> ").lower()
        if user_input == "an":
            key = input("Please enter the key:\n>> ")
            value = input("Please enter the value:\n>> ")
            bin_tree.insert_node(key, value)
            print("Node has been inserted successfully.\n")
        elif user_input == "gv":
            key = input("Please enter the key:\n>> ")
            print(f"The value of the key '{key}' is '{bin_tree.get_value(key)}'.")
        