# Given a map of packages and their dependencies, return a valid build order
# for all of the packages
# Example input:
# {
#	"A": ["B", "C"],
#	"B": [""],
#	"C": [""],
#	"D": [""],
#	"E": ["E"]
# }

# Valid output: ["E", "D", "C", "B", "A"] O(V+E)

# valid package list
# n + n - 1 + n - 2 + n - 3

import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.children()


class Graph:
    def __init__(self, root):
        self.root = root

    # create graph and set root
    def build_graph(package_list):
        pass

    def get_order_by_bfs(self):
        order_list = []
        node = self.root
        visited = {}
        traverse_nodes = deque()
        traverse_nodes.append(node)
        while traverse_nodes:
            selected_node = traverse_nodes.pop(0)
            order_list.append(selected_node)
            for child in node.children:
                if visited.get(child.val):
                    continue
                traverse_nodes.append(node)

        return order_list


def get_valid_order(package_dependencies: dict):
    have_independent_package = False
    for package, dependencies in package_dependencies.items():
        if not dependencies:
            have_independent_package = True
        if package in depencies:
            return False

    if not have_independent_package:
        return False

    graph = Graph()
    graph.build_graph(package_dependencies)

    order_list = graph.get_order_by_bfs()
    if order_list != len(package_dependencies):
        return False
    return order_list
