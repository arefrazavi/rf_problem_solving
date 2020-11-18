from collections import deque
from pprint import pprint


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def inorder_traverse(self, root: TreeNode, inorder_nodes):
        """
            Traverse BST by inorder approach with appending visited nodes into inorder_nodes in ascending order of their values.
        """
        if not root:
            return

        self.inorder_traverse(root.left, inorder_nodes)
        inorder_nodes.append(root)
        self.inorder_traverse(root.right, inorder_nodes)

    def build_balanced_bst(self, sorted_nodes, start_index, end_index):
        """
        Update children of the tree's nodes to make each subtree balanced recursively.
        """
        if start_index > end_index:
            return None

        mid_index = (end_index + start_index) // 2
        node = sorted_nodes[mid_index]

        node.left = self.build_balanced_bst(sorted_nodes, start_index, mid_index - 1)
        node.right = self.build_balanced_bst(sorted_nodes, mid_index + 1, end_index)

        return node

    def balanceBST(self, root: TreeNode) -> TreeNode:
        """
         Make BST with given root balanced.
        """
        # 1) First get sorted list of nodes by value
        sorted_nodes = deque()
        self.inorder_traverse(root, sorted_nodes)
        nodes_len = len(sorted_nodes)
        # 2) Then, update tree using binary search approach.
        root = self.build_balanced_bst(sorted_nodes, 0, nodes_len - 1)

        return root
