class Binary_Node:
    def __init__(self, key: str, value = None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

class Binary_Tree:
    def __init__(self):
        self.root = Binary_Node("root")
    
    def insert_node(self, key, value):
        #Add Node
    
    def delete_node(self, key):

    def get_value(self, key:str):
        if key:
            
        else:
            raise ValueError

if __name__ == "__main__":
    bin_tree = Binary_Tree()