import os
import sys
from pprint import pprint
import queue

# Python (or rather, the CPython implementation) doesn't optimize tail recursion, and unbridled recursion causes stack overflows.
# You can check the recursion limit with sys.getrecursionlimit
# Avoid error: RecursionError: maximum recursion depth exceeded in comparison
sys.setrecursionlimit(1500)


class Node:
    def __init__(self, data, left=None, right=None, depth=None):
        self.data = data
        self.left = left
        self.right = right
        self.depth = depth

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right


def create_binary_tree(indexes):
    tree_root = Node(data=1, depth=1)
    parent_nodes_queue = queue.Queue()
    parent_nodes_queue.put(tree_root)
    for children_indexes in indexes:
        current_parent_node = parent_nodes_queue.get()
        if children_indexes[0] != -1:
            child_node = Node(data=children_indexes[0], depth=(current_parent_node.depth + 1))
            current_parent_node.left = child_node
            parent_nodes_queue.put(child_node)
        if children_indexes[1] != -1:
            child_node = Node(data=children_indexes[1], depth=(current_parent_node.depth + 1))
            current_parent_node.right = child_node
            parent_nodes_queue.put(child_node)

    return tree_root


def swap_children_by_query(root: Node, query):
    # If query is multiple of root depth, swap root's children.
    if (root.depth % query) == 0:
        temp_node = root.left
        root.left = root.right
        root.right = temp_node

    if root.left:
        swap_children_by_query(root.left, query)

    if root.right:
        swap_children_by_query(root.right, query)


# visit nodes in left, root, right order.
def traverse_in_order(root: Node):
    visited_nodes_data = []
    if root.left:
        visited_nodes_data.extend(traverse_in_order(root.left))

    visited_nodes_data.append(root.data)

    if root.right:
        visited_nodes_data.extend(traverse_in_order(root.right))

    return visited_nodes_data


#
# Complete the swapNodes function below.
#
def swapNodes(indexes, queries):
    root = create_binary_tree(indexes)

    results = []
    for query in queries:
        swap_children_by_query(root, query)
        visited_nodes_data = traverse_in_order(root)
        results.append(visited_nodes_data)

    return results


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    results = swapNodes(indexes, queries)

    for result in results:
        print(*result, sep=' ')
    # fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    # fptr.write('\n')
    #
    # fptr.close()
