from pprint import pprint


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.level = None
        self.parent = None


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        search_nodes = {}
        if root.val == x or root.val == y:
            return False
        root.level = 1
        self.find_nodes_by_bfs(root, x, y, search_nodes)

        has_same_level = (search_nodes[x].level == search_nodes[y].level)
        has_diff_parents = (search_nodes[x].parent.val != search_nodes[y].parent.val)
        if has_same_level and has_diff_parents:
            return True

        return False

    def find_nodes_by_bfs(self, root: TreeNode, x: int, y: int, search_nodes={}):
        if not root:
            return False

        if root.val == x:
            search_nodes[x] = root
        elif root.val == y:
            search_nodes[y] = root

        if search_nodes.get(x) and search_nodes.get(y):
            return True

        if root.left:
            root.left.parent = root
            root.left.level = root.level + 1

        if root.right:
            root.right.parent = root
            root.right.level = root.level + 1

        self.find_nodes_by_bfs(root.left, x, y, search_nodes)
        self.find_nodes_by_bfs(root.right, x, y, search_nodes)


