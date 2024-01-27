from node import Node
from binary_tree import BinaryTree

tree = BinaryTree(Node(9))
tree.add(Node(5))
tree.add(Node(11))
tree.add(Node(3))
tree.add(Node(23))
tree.add(Node(12))
tree.add(Node(8))
tree.add(Node(30))

tree.inorder()