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
#            self.insert_recursive(data, self.root)
            self.insert_recursive(data, self.root)

    def _insert_recursive(self, data, current_node):
        """
        Recursive helper function to insert a new node with data at the correct position.
        """
        if data < current_node.data:
            # If data is less than current node, go left
            if current_node.left is None:
                current_node.left = TreeNode(data)
            else:
                self._insert_recursive(data, current_node.left)
        elif data > current_node.data:
            # If data is greater than current node, go right
            if current_node.right is None:
                current_node.right = TreeNode(data)
            else:
                self._insert_recursive(data, current_node.right)
