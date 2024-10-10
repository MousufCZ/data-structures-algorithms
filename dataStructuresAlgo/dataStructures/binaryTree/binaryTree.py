class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self.insert_recursive(data, self.root)

    def insert_recursive(self, data, current_node):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = TreeNode(data)
            else:
                self.insert_recursive(data, current_node.left)
        elif data > current_node.data:
            if current_node.right is None:
                current_node.right = TreeNode(data)
            else:
                self.insert_recursive(data, current_node.right)

    def delete(self, data):
        self.root = self.delete_recursive(data, self.root)

    def delete_recursive(self, data, current_node):
        if current_node is None:
            return current_node

        if data < current_node.data:
            current_node.left = self.delete_recursive(data, current_node.left)
        elif data > current_node.data:
            current_node.right = self.delete_recursive(data, current_node.right)
        else:
            # Node to be deleted found
            if current_node.left is None:
                return current_node.right
            elif current_node.right is None:
                return current_node.left

            # Node has two children, find the successor (minimum value in the right subtree)
            current_node.data = self.find_min(current_node.right)
            # Delete the successor from the right subtree
            current_node.right = self.delete_recursive(current_node.data, current_node.right)

        return current_node

    def find_min(self, node):
        current = node
        while current.left:
            current = current.left
        return current.data

    def search(self, data):
        return self.search_recursive(data, self.root)

    def search_recursive(self, data, current_node):
        if current_node is None or current_node.data == data:
            return current_node

        if data < current_node.data:
            return self.search_recursive(data, current_node.left)
        else:
            return self.search_recursive(data, current_node.right)

    def depth_first_traversal(self, order):
        if order == "preorder":
            self.pre_order_traversal(self.root)
        elif order == "inorder":
            self.in_order_traversal(self.root)
        elif order == "postorder":
            self._post_order_traversal(self.root)

    def pre_order_traversal(self, node):
        """
        Helper function for pre-order traversal: Visit the current node, then left subtree, then right subtree.
        """
        if node:
            print(node.data)
            self.pre_order_traversal(node.left)
            self.pre_order_traversal(node.right)

    def in_order_traversal(self, node):
        """
        Helper function for in-order traversal: Visit left subtree, then current node, then right subtree.
        """
        if node:
            self.in_order_traversal(node.left)
            print(node.data)
            self.in_order_traversal(node.right)

    def _post_order_traversal(self, node):
        """
        Helper function for post-order traversal: Visit left subtree, then right subtree, then current node.
        """
        if node:
            self._post_order_traversal(node.left)
            self._post_order_traversal(node.right)
            print(node.data)

def test_binary_tree():
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