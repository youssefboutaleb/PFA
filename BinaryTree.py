from Node import Node
class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, data, path):
        # If the tree is empty, create the root node
        if self.root is None:
            self.root = Node(data)
        else:
            # Set the current node to the root of the tree
            current_node = self.root

            # Follow the path to find the correct parent node for the new node
            for direction in path:
                if direction == "L":
                    if current_node.left is None:
                        current_node.left = Node()
                    current_node = current_node.left
                elif direction == "R":
                    if current_node.right is None:
                        current_node.right = Node()
                    current_node = current_node.right

            # Set the data for the new node
            current_node.data = data

    def print_preorder(self):
        if self.root is not None:
            self._print_preorder(self.root)
        print()

    def _print_preorder(self, node):
        print(node.data, end=" ")
        if node.left is not None:
            self._print_preorder(node.left)
        if node.right is not None:
            self._print_preorder(node.right)







