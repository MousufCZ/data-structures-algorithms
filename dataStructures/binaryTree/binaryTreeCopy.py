

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
        """
        BinaryTree constructor to initialize an empty binary tree.
        """
        self.root = None

    def insert(self, data):
        """
        Insertion operation to add a new node with data to the binary tree.
        """
        if not self.root:
            # If the tree is empty, set the new node as the root
            self.root = TreeNode(data)
        else:
            # Otherwise, recursively find the appropriate position to insert the new node
            self._insert_recursive(data, self.root)

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

    def delete(self, data):
        """
        Deletion operation to remove a node with the given data from the binary tree.
        """
        self.root = self._delete_recursive(data, self.root)

    def _delete_recursive(self, data, current_node):
        """
        Recursive helper function to delete a node with the given data from the binary tree.
        """
        if current_node is None:
            return current_node

        if data < current_node.data:
            current_node.left = self._delete_recursive(data, current_node.left)
        elif data > current_node.data:
            current_node.right = self._delete_recursive(data, current_node.right)
        else:
            # Node to be deleted found
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            # Node has two children, find the successor (minimum value in the right subtree)
            current_node.data = self._find_min(current_node.right)
            # Delete the successor from the right subtree
            current_node.right = self._delete_recursive(current_node.data, current_node.right)

        return current_node

    def _find_min(self, node):
        """
        Helper function to find the minimum value in a binary tree rooted at the given node.
        """
        current = node
        while current.left:
            current = current.left
        return current.data

    def search(self, data):
        """
        Searching operation to find a node with the given data in the binary tree.
        """
        return self._search_recursive(data, self.root)

    def _search_recursive(self, data, current_node):
        """
        Recursive helper function to search for a node with the given data in the binary tree.
        """
        if current_node is None or current_node.data == data:
            return current_node

        if data < current_node.data:
            return self._search_recursive(data, current_node.left)
        else:
            return self._search_recursive(data, current_node.right)

    def depth_first_traversal(self, order):
        """
        Depth-First Traversal (DFS) operation to visit nodes of the binary tree in pre-order, in-order, or post-order.
        """
        if order == "preorder":
            self._pre_order_traversal(self.root)
        elif order == "inorder":
            self._in_order_traversal(self.root)
        elif order == "postorder":
            self._post_order_traversal(self.root)

    def _pre_order_traversal(self, node):
        """
        Helper function for pre-order traversal: Visit the current node, then left subtree, then right subtree.
        """
        if node:
            print(node.data)
            self._pre_order_traversal(node.left)
            self._pre_order_traversal(node.right)

    def _in_order_traversal(self, node):
        """
        Helper function for in-order traversal: Visit left subtree, then current node, then right subtree.
        """
        if node:
            self._in_order_traversal(node.left)
            print(node.data)
            self._in_order_traversal(node.right)

    def _post_order_traversal(self, node):
        """
        Helper function for post-order traversal: Visit left subtree, then right subtree, then current node.
        """
        if node:
            self._post_order_traversal(node.left)
            self._post_order_traversal(node.right)
            print(node.data)

def test_binary_tree():
    """
    Function to test the binary tree operations.
    """
    bt = BinaryTree()
    bt.insert(5)
    bt.insert(3)
    bt.insert(7)
    bt.insert(2)
    bt.insert(4)
    bt.insert(6)
    bt.insert(8)

    print("In-order Traversal:")
    bt.depth_first_traversal("inorder")

    print("\nPre-order Traversal:")
    bt.depth_first_traversal("preorder")

    print("\nPost-order Traversal:")
    bt.depth_first_traversal("postorder")

    print("\nSearching for value 4:", bt.search(4).data)
    print("Searching for value 10:", bt.search(10))

    bt.delete(3)
    print("\nIn-order Traversal after deleting 3:")
    bt.depth_first_traversal("inorder")

if __name__ == "__main__":
    test_binary_tree()