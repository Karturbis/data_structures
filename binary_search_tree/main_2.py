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


class BinaryNode:
    def __init__(self, key: str, parent_key: str, value=None):
        self.key = key
        self.parent_key = parent_key
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

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

    def get_node(self, key: str, start_node=None) -> BinaryNode:
        """Returns the node with the given key,
        if no node with given key exists, it
        returns the last existent node on the path
        and raises a Node not found Exception."""
        if not start_node:
            start_node = self.__root
        if start_node:
            if key == start_node.key:
                node = start_node
            else:
                try:
                    node = self.__get_node_inner(key, start_node)
                except NodeNotFoundException:
                    return self.__get_node_backpass_variable, False
            return node, True
        # else:
        raise EmptyTreeException

    def __get_node_inner(self, key: str, position) -> BinaryNode:
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
                node.left = BinaryNode(key, node.key, value)
            else:
                node.right = BinaryNode(key, node.key, value)
        else:
            self.__root = BinaryNode(key, None, value)

    def get_minimum_node(self, start_key=None) -> BinaryNode:
        if not start_key:
            start_key = self.__root
        running_node = start_key
        while True:
            if running_node.left:
                running_node = running_node.left
            else:
                return running_node

    def delete_node(self, key: str, start_node=None) -> None:
        node = self.get_node(key, start_node)
        if node[1]:

            node = node[0]
            if node.key == self.__root.key:
                raise NotImplementedError
            else:
                parent = self.get_node(node.parent_key)[0]
            if node.key < parent.key:
                parent.left = None
            else:
                parent.right = None
            if not(node.left and node.right):
                node = None
            elif node.left and not node.right:
                node = node.left
            elif not node.left and node.right:
                node = node.right
            else:
                node = self.get_minimum_node(node)
                self.delete_node(node.key, node.left)
        else:
            raise NodeNotFoundException("Node could not be removed from tree.")


if __name__ == "__main__":
    search_tree = BinarySearchTree()
    names = ["caspian", "domo", "lukas", "ziana", "merle", "alexa", "michel"]

    for name in names:
        search_tree.add_node(name, len(name))
    
    search_tree.delete_node("domo")

    for name in names:
        print(search_tree.get_value(name))

