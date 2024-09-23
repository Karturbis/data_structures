"""For most recent Sourcecode visit:
https://github.com/Karturbis/data_structures/tree/main/binary_search_tree
"""

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
    """Dataclass, instances of which are
    BinaryNodes, that can be used in a Binary Tree."""
    def __init__(self, key: str, parent_key: str, value=None):
        self.key = key
        self.parent_key = parent_key
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """A Binary Search tree, with methods
    to operate on."""

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
        """Inner method for the get_node() method.
        Recursivly searches for a Node."""
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
        """Creates a BinaryNode with the given
        values and inserts it into the BinarySearchTree."""
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
        """Adds all Nodes of a subtree to
        the main tree.
        Used by the delete_node() method."""
        running_tree = start_node
        while True:
            self.add_node(running_tree.key, running_tree.value)
            if not running_tree.right:
                break

    def get_minimum_node(self, start_key=None) -> BinaryNode:
        """Returns the Node woth the smallest value of the
        Subtree of a given Node, of no Node is passed, it
        starts a the root node.
        Used by the delete_node() method."""
        if not start_key:
            start_key = self.__root
        running_node = start_key
        while True:
            if running_node.left:
                running_node = running_node.left
            else:
                return running_node

    def get_maximum_node(self, start_key=None) -> BinaryNode:
        """Returns the Node woth the biggest value of the
        Subtree of a given Node, of no Node is passed, it
        starts a the root Node.
        Important for my teacher."""
        if not start_key:
            start_key = self.__root
        running_node = start_key
        while True:
            if running_node.right:
                running_node = running_node.right
            else:
                return running_node

    def set_val(self, obj0, subobj0: str, value, subsubobj0: str = None):
        """Sets the value of the subobject subobj0 of the object obj0
        to the value value, if subsubobj0 is passed it sets the value
        of the subobject of the subobject of obj0. This only works, if
        subsubobj0 is 'left', because other cases are not needed.
        This method is only used by the delete_node() method."""
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
        """Deletes the Node with the given key in the subtree
        of the given start_node, if no start_node is passed,
        it starts at the root Node."""
        node = self.get_node(key, start_node)
        if node[1]:  # If the Node is in the Tree
            node = node[
                0
            ]  # set node to the Node object, which is in [0] of the node tuple
            if self.__root:
                has_parent = False
                pathway = None
            else:
                has_parent = True
                old_parent = self.get_node(node.parent_key)[0]
                if node.key < old_parent.key:
                    pathway = "left"
                elif node.key > old_parent.key:
                    pathway = "right"
            if not (node.left or node.right):
                if has_parent:
                    self.set_val(old_parent, pathway, None)
                else:
                    self.__root = None
            elif node.left and not node.right:
                if has_parent:
                    self.set_val(old_parent, pathway, node.left)
                    self.set_val(old_parent, pathway, old_parent.key, "parent_key")
                else:
                    self.__root = node.left
            elif not node.left and node.right:
                if has_parent:
                    self.set_val(old_parent, pathway, node.right)
                    self.set_val(old_parent, pathway, old_parent.key, "parent_key")
                else:
                    self.__root = node.right
            else:  # not node.left and not node.right
                if has_parent:
                    self.set_val(old_parent, pathway, self.get_minimum_node(node.right))
                else:
                    self.__root = self.get_minimum_node(node.right)
                if not pathway:
                    old_parent_of_minimum = self.get_node(self.__root.parent_key)
                elif pathway == "left":
                    old_parent_of_minimum = self.get_node(old_parent.left.parent_key)
                elif pathway == "right":
                    old_parent_of_minimum = self.get_node(old_parent.right.parent_key)
                old_parent_of_minimum[0].left = None
                if has_parent:
                    self.set_val(old_parent, pathway, old_parent.key, "parent_key")
                    self.set_val(old_parent, pathway, node.left, "left")
                else:
                    self.__root.left = node.left
                old_min_right_subtree = None
                if not pathway:
                    if self.__root.right:
                        old_min_right_subtree = self.__root.right
                    self.__root.right = node.right
                elif pathway == "left":
                    if old_parent.left.right:
                        old_min_right_subtree = old_parent.left.right
                    old_parent.left.right = node.right
                elif pathway == "right":
                    if old_parent.right.right:
                        old_min_right_subtree = old_parent.right.right
                    old_parent.right.right = node.right
                if old_min_right_subtree:
                    self.__add_subtree(old_min_right_subtree.right)
            self.__root.parent_key = None
        else:
            raise NodeNotFoundException("Node could not be removed from tree.")


class ThisClassIsNeccessaryAndIDoNotKnowWhyButICodeItAnyway:
    """Class which contains all user input related stuff."""

    def __init__(self, bin_tree):
        self.commands = {
            "add": [bin_tree.add_node, "add_node"],
            "delete": [bin_tree.delete_node, "delete_node"],
            "find": [bin_tree.get_value, "get_value"],
            "help": [self.help, "help"]
        }

    def help(self):
        """Prints all available commands to the terminal."""
        for key, value in self.commands.items():
            print(f"{key}: {value[1]}")

    def input_loop(self, bin_tree):
        """Takes user input and calls the appropriate
        methods with the given arguments."""
        while True:
            commands_input = input("> ").lower().split(" ")
            if commands_input == [""]:
                continue
            elif commands_input[0] == "?":
                self.help()
            elif commands_input[0] == "q":
                break
            elif len(commands_input) > 1:
                for key, func_iter in self.commands.items():
                    if key.startswith(commands_input[0]):
                        print(func_iter[0](*commands_input[1:]))
            elif len(commands_input) == 1:
                for key, func_iter in self.commands.items():
                    if key.startswith(commands_input[0]):
                        print(func_iter[0]())


def main():
    """Main method, initializes
    an instance of BinarySearchTree
    and one of the Input Handler."""
    bin_tree = BinarySearchTree()
    dumbassinputhandler = ThisClassIsNeccessaryAndIDoNotKnowWhyButICodeItAnyway(bin_tree)
    dumbassinputhandler.input_loop(bin_tree)

if __name__ == "__main__":
    main()
