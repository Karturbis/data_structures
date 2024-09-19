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
        return "The node was not found!"

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

    def __add_subtree(self, start_node):
        running_tree = start_node
        while True:
            self.add_node(running_tree.key, running_tree.value)
            if not running_tree.right:
                break

    def get_minimum_node(self, start_key=None) -> BinaryNode:
        if not start_key:
            start_key = self.__root
        running_node = start_key
        while True:
            if running_node.left:
                running_node = running_node.left
            else:
                return running_node

    def set_val(self, obj0, subobj0: str, value, subsubobj0: str=None):
        if subobj0 == "left" and obj0.left:
            if subsubobj0 == "parent_key":
                obj0.left.parent_key = value
            elif subsubobj0 == "left":
                obj0.left.left = value
            elif not subsubobj0:
                obj0.left = value
        elif subobj0 == "right" and obj0.right:
            if subsubobj0 == "parent_key":
                obj0.right.parent_key = value
            elif subsubobj0 == "left":
                obj0.right.left = value
            elif not subsubobj0:
                obj0.right = value
        else:
            raise NodeNotFoundException()

    def delete_node(self, key: str, start_node=None) -> None:
        node = self.get_node(key, start_node)
        if node[1]:  # If the Node is in the Tree
            node = node[0]  # set node to the Node object, which is in [0] of the node tuple
            if node.key == self.__root.key:
                self.__root = node
                self.__root.parent_key = None
            else:
                old_parent = self.get_node(node.parent_key)[0]
                if node.key < old_parent.key:
                    pathway = "left"
                elif node.key > old_parent.key:
                    pathway = "right"
                if not (node.left or node.right):
                    self.set_val(old_parent, pathway, None)
                elif node.left and not node.right:
                    self.set_val(old_parent, pathway, node.left)
                    self.set_val(old_parent, pathway, old_parent.key, "parent_key")
                elif not node.left and node.right:
                    self.set_val(old_parent, pathway, node.right)
                    self.set_val(old_parent, pathway, old_parent.key, "parent_key")
                else:  # not node.left and not node.right
                    self.set_val(old_parent, pathway, self.get_minimum_node(node.right))
                    if pathway == "left":
                        old_parent_of_minimum = self.get_node(old_parent.left.parent_key)
                    else:
                        old_parent_of_minimum = self.get_node(old_parent.right.parent_key)
                    old_parent_of_minimum[0].left = None
                    self.set_val(old_parent, pathway, old_parent.key, "parent_key")
                    self.set_val(old_parent, pathway, node.left, "left")
                    old_min_right_subtree = None
                    if pathway == "left":
                        if old_parent.left.right:
                            old_min_right_subtree = old_parent.left.right
                        old_parent.left.right = node.right
                    else:
                        if old_parent.right.right:
                            old_min_right_subtree = old_parent.right.right
                        old_parent.right.right = node.right
                    if old_min_right_subtree:
                        self.__add_subtree(old_min_right_subtree.right)
        else:
            raise NodeNotFoundException("Node could not be removed from tree.")


if __name__ == "__main__":
    search_tree = BinarySearchTree()
    names = [
        "krypto30",
        "aqua41",
        "martian55",
        "cat40",
        "lantern90",
        "thebat39",
        "flash44",
        "rex40",
        "wonder11",
    ]

    for name in names:
        search_tree.add_node(name, len(name))

    search_tree.delete_node("krypto30")

    for name in names:
        print(search_tree.get_value(name))
