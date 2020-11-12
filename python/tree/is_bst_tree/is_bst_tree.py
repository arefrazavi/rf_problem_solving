# https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=trees

""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

import sys

sys.setrecursionlimit(1500)


def checkBST(root):
    data_visited = {}
    is_bst, min_val, max_val = is_bst_tree(root, data_visited)

    return is_bst


def is_bst_tree(node, data_visited):
    # if node:
    #     print('Node: ', end=': ')
    #     print(node.data, end=' => ')
    #     if node.left:
    #         print('Left: ' + str(node.left.data), end=' ')
    #     if node.right:
    #         print('Right: ' + str(node.right.data), end =' ')
    #     print()

    # If there is no node
    if not node:
        return True, float('-inf'), float('inf')

    # If node data is repeated
    if data_visited.get(node.data):
        return False, float('-inf'), float('inf')
    data_visited[node.data] = True

    left_min = node.data
    right_max = node.data
    if node.left:
        is_bst, left_min, left_max = is_bst_tree(node.left, data_visited)
        if not is_bst or node.data < left_max:
            return False, float('-inf'), float('inf')

    if node.right:
        is_bst, right_min, right_max = is_bst_tree(node.right, data_visited)
        if not is_bst or node.data > right_min:
            return False, float('-inf'), float('inf')

    return True, left_min, right_max
