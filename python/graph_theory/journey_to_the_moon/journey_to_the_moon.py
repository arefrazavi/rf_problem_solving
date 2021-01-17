#!/bin/python3

import math
import os
import random
import re
import sys
from pprint import pprint
from collections import defaultdict

sys.setrecursionlimit(1500)


class Node:
    def __init__(self, data):
        self.data = data
        self.neighbors = []


# Complete the journeyToMoon function below.
def journeyToMoon(n, same_country_astronaut):
    ast_nodes = {}
    for pair in same_country_astronaut:
        if not ast_nodes.get(pair[0]):
            ast_nodes[pair[0]] = Node(pair[0])
        if not ast_nodes.get(pair[1]):
            ast_nodes[pair[1]] = Node(pair[1])
        ast_nodes[pair[0]].neighbors.append(ast_nodes[pair[1]]);
        ast_nodes[pair[1]].neighbors.append(ast_nodes[pair[0]]);

    visited = {}
    astronauts_by_country = []
    for ast_index, ast_node in ast_nodes.items():
        # print(ast_node.data, end=': ')
        # for node in ast_node.neighbors:
        #     print(node.data, end=', ')
        # print()
        if not visited.get(ast_node.data):
            same_country_astronauts = []
            dfs_explore(ast_node, same_country_astronauts, visited)
            astronauts_by_country.append(same_country_astronauts)

    # pprint(astronauts_by_country)
    different_country_pair_count = (n * (n - 1)) / 2
    for same_country_astronauts in astronauts_by_country:
        same_country_astronauts_len = len(same_country_astronauts)
        different_country_pair_count -= same_country_astronauts_len * (same_country_astronauts_len - 1) / 2

    return int(different_country_pair_count)


def dfs_explore(node, same_country_astronauts, visited):
    visited[node.data] = True
    same_country_astronauts.append(node.data)
    for neighbor_node in node.neighbors:
        if not visited.get(neighbor_node.data):
            dfs_explore(neighbor_node, same_country_astronauts, visited)


if __name__ == '__main__':
    file_path = 'input'
    file = open(file_path, 'r')
    file_content = file.read()
    rows = file_content.split('\n')

    np = rows[0].split()
    n = int(np[0])
    p = int(np[1])
    astronaut = []
    for i in range(p):
        astronaut.append(list(map(int, rows[i + 1].rstrip().split())))

    result = journeyToMoon(n, astronaut)

    print(result)
