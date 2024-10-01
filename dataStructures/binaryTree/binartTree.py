class TreeNode:
    def __init__(self, data):
        """
        TreeNode constructor to initialize a node with data.
        """
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            # If the tree is empty, set the new node as the root
            self.root = TreeNode(data)
        else:
            # Otherwise, recursively find the appropriate position to insert the new node
            self.insert_recursive(data, self.root)

    