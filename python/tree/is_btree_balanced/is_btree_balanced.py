# https://leetcode.com/problems/balanced-binary-tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def get_is_balanced_and_height(self, root: TreeNode) -> (bool, int):
        if not root or (not root.left and not root.right):
            return (True, 0)
        if root.left:
            (is_left_balanced, left_height) = self.get_is_balanced_and_height(root.left)
            # Add current edge between root nad left child to left height.
            left_height += 1
        else:
            (is_left_balanced, left_height) = (True, 0)

        if root.right:
            (is_right_balanced, right_height) = self.get_is_balanced_and_height(root.right)
            # Add current edge between root nad right child to right height.
            right_height += 1
        else:
            (is_right_balanced, right_height) = (True, 0)

        is_balanced = is_left_balanced & is_right_balanced

        if abs(left_height - right_height) > 1:
            is_balanced = False

        height = max(left_height, right_height)

        print(root.val, end=' => ')
        print(is_balanced, end=' : ')
        print(height)

        return (is_balanced, height)

    def isBalanced(self, root: TreeNode) -> bool:
        """
        Check if the tree with given root is balanced,
        i.e. the left and right heights of the root differ by at most 1, and
        rhe left and trees are balanced themselves.
        """
        (is_balanced, height) = self.get_is_balanced_and_height(root)

        return is_balanced