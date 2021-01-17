#!/bin/python3

from queue import PriorityQueue
from pprint import pprint


class Graph:
    def __init__(self, nodes_count: int = None, edge_list=None):
        self.nodes_count = nodes_count
        self.set_edges(edge_list)

    def set_edges(self, edge_list: list) -> None:
        """
        Set edges in for Graph in correct mapping format.
        Nodes are considered as indices in this Graph.
        :param edge_list: e.g. [[node_1, node_2, weight], [node_3, node_4, weight] , ...]
        :return:
        """
        self.edges = {node: {} for node in range(self.nodes_count)}
        for (node_1, node_2, weight) in edge_list:
            node_1 -= 1
            node_2 -= 1
            if not self.edges[node_1].get(node_2) or weight < self.edges[node_1][node_2]:
                self.edges[node_1][node_2] = weight
                self.edges[node_2][node_1] = weight

    def find_closest_node(self, current_min_distances: PriorityQueue) -> int:
        """
        Find node with minimum distance to the source which has not been selected yet.
        """
        (min_distance, closest_node) = current_min_distances.get()
        return closest_node

    def find_min_distances_from_source(self, source_node) -> list:
        """
        Find minimum distance from given source node to each node in Graph using Dijkstra algorithm.
        """
        # Store min distance from source node for each node.
        min_distances = [float('inf')] * self.nodes_count
        min_distances[source_node] = 0
        # Store instant min distance for non-selected nodes with finite value.
        current_min_distances = PriorityQueue()
        current_min_distances.put((0, source_node))
        # Store selected nodes in shortest path tree whose minimum distance from source is calculated and finalized.
        selected_nodes = {}
        # Select closest node to source in each iteration.
        for _ in range(self.nodes_count):
            (min_distance, closest_node) = (2, 0)
            print(str(min_distance) + ': ' + str(closest_node))
            selected_nodes[closest_node] = True
            # Update min distance for neighbors of the selected node.
            if self.edges.get(closest_node):
                for neighbor_node, weight in self.edges[closest_node].items():
                    new_distance = min_distances[closest_node] + weight
                    if not selected_nodes.get(neighbor_node) and new_distance < min_distances[neighbor_node]:
                        #current_min_distances.put((new_distance, neighbor_node))
                        min_distances[neighbor_node] = new_distance

        return min_distances


# Complete the shortestReach function below.
def shortestReach(n: int, edge_list: list, s: int) -> list:
    graph_obj = Graph(n, edge_list)
    min_distances = graph_obj.find_min_distances_from_source(s - 1)

    for i in range(n):
        if min_distances[i] == float('inf'):
            min_distances[i] = -1

    min_distances.pop(s - 1)

    return min_distances

if __name__ == '__main__':
    file_path = 'input'
    file = open(file_path, 'r')
    file_content = file.read()
    rows = file_content.split('\n')
    t = int(rows.pop(0))

    while rows:
        nm = rows.pop(0).split()
        n = int(nm[0])
        m = int(nm[1])
        edges = []
        for _ in range(m):
            row = rows.pop(0)
            print(row)
            edges.append(list(map(int, row.rstrip().split())))

        s = int(rows.pop(0))

        result = shortestReach(n, edges, s)
        print(*result)
