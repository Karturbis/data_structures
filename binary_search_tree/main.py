class Binary_Node:
    def __init__(self, name: str, value = None):
        self.name = name
        self.value = value
        self.left = None
        self.right = None

class Binary_Tree:
    def __init__(self):
        self.root = Binary_Node("root")
    
    def insert_node(self, name, value):
        #Add Node
    
    def delete_node(self, name):

    def get_value(self, key:str):
        if key:
        else:
            raise ValueError

if __name__ == "__main__":
    bin_tree = Binary_Tree()