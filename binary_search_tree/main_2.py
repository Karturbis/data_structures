class EmptyTreeException(Exception):
    """This Excepiotn is thrown, when
    the given tree is empty, but the
    called function needs a non empty
    tree to operate on."""


class NodeNotFoundException(Exception):
    """Raised, when the searched Node
    could not be found."""


class DuplicateKeyException(Exception):
    """Raised, when someone is trying to
    add a node with a key, that already
    exists."""


class Binary_Node:
    def __init__(self, key: str, parent_key: str, value=None):
        self.key = key
        self.parent_key = parent_key
        self.value = value
        self.left = None
        self.right = None


class Binary_Search_Tree:

    def __init__(self):
        self.__root = None
        self.__get_node_backpass_variable = None

    def get_value(self, key: str):
        """Returns the value of the node with
        the given key."""
        node = self.get_node(key)
        if node[1]:
            return node[0].value
        # else:
        raise NodeNotFoundException

    def get_node(self, key: str) -> Binary_Node:
        """Returns the node with the given key,
        if no node with given key exists, it
        returns the last existent node on the path
        and raises a Node not found Exception."""
        if self.__root:
            if key == self.__root.key:
                node = self.__root
            else:
                try:
                    node = self.__get_node_inner(key, self.__root)
                except NodeNotFoundException:
                    return self.__get_node_backpass_variable, False
            return node, True
        # else:
        raise EmptyTreeException

    def __get_node_inner(self, key: str, position) -> Binary_Node:
        if key < position.key:
            if position.left:
                if key == position.left.key:
                    return position.left
                # else:
                return self.__get_node_inner(key, position.left)
            # else:
            self.__get_node_backpass_variable = position
            raise NodeNotFoundException()
        # else:
        if position.right:
            if key == position.right.key:
                return position.right
            # else:
            return self.__get_node_inner(key, position.right)
        # else:
        self.__get_node_backpass_variable = position
        raise NodeNotFoundException(position)

    def add_node(self, key: str, value=None) -> None:
        if self.__root:
            node = self.get_node(key)
            if node[1]:
                raise DuplicateKeyException
            # else:
            node = node[0]
            if key < node.key:
                node.left = Binary_Node(key, node.key, value)
            else:
                node.right = Binary_Node(key, node.key, value)
        else:
            self.__root = Binary_Node(key, None, value)

    def delete_node(self, key: str) -> None:
        pass

if __name__ == "__main__":
    search_tree = Binary_Search_Tree()
    search_tree.add_node("caspian", 18)
    search_tree.add_node("domo", 17)
    print(search_tree.get_value("caspian"))
    print(search_tree.get_value("domo"))
