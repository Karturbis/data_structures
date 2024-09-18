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
        self.root = None

    def get_value(self, key: str):
        """Returns the value of the node with
        the given key."""
        node = self.get_node(key)
        if node[1]:
            return node.value
        # else:
        raise NodeNotFoundException

    def get_node(self, key: str) -> Binary_Node:
        """Returns the node with the given key,
        if no node with given key exists, it
        returns the last existent node on the path
        and raises a Node not found Exception."""
        if self.root:
            if key == self.root.key:
                node = self.root
            else:
                try:
                    node = self.__get_node_inner(key, self.root)
                except NodeNotFoundException as parent:
                    return parent, False
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
            raise NodeNotFoundException(position)
        # else:
        if position.right:
            if key == position.right.key:
                return position.right
            # else:
            return self.__get_node_inner(key, position.right)
        # else:
        raise NodeNotFoundException(position)

    def add_node(self, key: str, value=None) -> None:
        if self.root:
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
            self.root = Binary_Node(key, None, value)

    def delete_node(self, key: str) -> None:
        pass
