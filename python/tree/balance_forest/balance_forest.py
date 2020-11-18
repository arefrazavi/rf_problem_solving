#!/bin/python3

import os
from pprint import pprint

class Tree:
    def __init__(self, size, weights):
        self.root = 0
        self.next_node_index = 0
        self.nodes_count = size
        self.edges_count = 0
        self.edges = [set([]) for _ in range(self.nodes_count)]
        self.weights = weights
        self.labels = [None] * self.nodes_count
        self.cumulative_weights = [None] * self.nodes_count
        self.removed_edges = [False] * self.nodes_count
        self.nodes_children_count = [None] * self.nodes_count

    def add_edge(self, node_index, neighbor_index):
        if neighbor_index not in self.edges[node_index]:
            self.edges[node_index].add(neighbor_index)
            self.edges[neighbor_index].add(node_index)
            self.edges_count += 1

    def initialize(self):
        self.set_labels(self.root)

    def set_labels(self, root):
        self.dfs(root, set([]))
        self.total_weight = self.cumulative_weights[self.root]
        for i, cw in enumerate(self.cumulative_weights):
            if cw > self.total_weight - cw:
                self.cumulative_weights[i] = self.total_weight - cw
                self.removed_edges[i] = True

    def dfs(self, node_index, visited):
        visited.add(node_index)
        self.labels[node_index] = self.next_node_index
        self.next_node_index += 1
        self.cumulative_weights[node_index] = self.weights[node_index]
        self.nodes_children_count[node_index] = 0
        for neighbor_index in self.neighbors(node_index):
            if neighbor_index not in visited:
                cw, neighbor_children_count = self.dfs(neighbor_index, visited)
                self.cumulative_weights[node_index] += cw
                self.nodes_children_count[node_index] += neighbor_children_count + 1
        return self.cumulative_weights[node_index], self.nodes_children_count[node_index]

    def neighbors(self, node_index):
        for neighbor_index in self.edges[node_index]:
            yield neighbor_index


def bin_search(nodes, weights, target_weight):
    first_index = 0
    nodes_count = len(nodes)
    last_index = nodes_count - 1
    while first_index < last_index:
        mid_index = (first_index + last_index) // 2
        if weights[nodes[mid_index]] >= target_weight:
            last_index = mid_index
        else:
            first_index = mid_index + 1

    return first_index if first_index < nodes_count else None


# Complete the balancedForest function below.
def balancedForest(node_weights, edges):
    nodes_len = len(node_weights)
    tree = Tree(nodes_len, node_weights)
    for edge in edges:
        tree.add_edge(edge[0] - 1, edge[1] - 1)
    tree.initialize()

    sorted_nodes = sorted(list(range(tree.nodes_count)), key=lambda x: tree.cumulative_weights[x])
    new_root_index = bin_search(sorted_nodes, tree.cumulative_weights, ((tree.total_weight + 2) // 3))
    if new_root_index is None:
        return -1
    while new_root_index < tree.nodes_count:
        new_root = sorted_nodes[new_root_index]
        new_root_cumulative_weight = tree.cumulative_weights[new_root]
        new_root_label = tree.labels[new_root]
        last_child_label = new_root_label + tree.nodes_children_count[new_root]

        for target_weight in (tree.total_weight - new_root_cumulative_weight * 2, new_root_cumulative_weight):
            next_node_index = bin_search(sorted_nodes, tree.cumulative_weights, target_weight)
            if next_node_index is not None:
                while (next_node_index < tree.nodes_count
                       and tree.cumulative_weights[sorted_nodes[next_node_index]] == target_weight):
                    second = sorted_nodes[next_node_index]
                    is_child = new_root_label < tree.labels[second] <= last_child_label
                    is_child = is_child if not tree.removed_edges[new_root] else not is_child
                    if not is_child and tree.labels[second] != new_root_label:
                        return new_root_cumulative_weight * 3 - tree.total_weight
                    next_node_index += 1

        new_root_index += 1
    if 2 * new_root_cumulative_weight == tree.total_weight:
        return new_root_cumulative_weight
    return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        c = list(map(int, input().rstrip().split()))

        edges = []

        for _ in range(n - 1):
            edges.append(list(map(int, input().rstrip().split())))

        result = balancedForest(c, edges)

        fptr.write(str(result) + '\n')

    fptr.close()
