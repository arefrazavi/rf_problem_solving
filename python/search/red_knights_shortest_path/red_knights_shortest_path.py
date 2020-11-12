#!/bin/python3

import queue
from pprint import pprint


# Complete the printShortestPath function below.
def printShortestPath(n, i_start, j_start, i_end, j_end):
    start_cell = [i_start, j_start]
    bfs_queue = queue.Queue()
    bfs_queue.put(start_cell)
    visited = {get_cell_id(start_cell[0], start_cell[1]): {'cell': start_cell, 'parent_cell': None, 'move': None}}
    destination_reached = 0
    while not bfs_queue.empty():
        print(bfs_queue.qsize())
        current_cell = bfs_queue.get()
        visit_cell(current_cell[0] - 2, current_cell[1] - 1, n, 'UL', current_cell, visited, bfs_queue)
        if current_cell[0] - 2 == i_end and current_cell[1] - 1 == j_end:
            destination_reached = 1
            break

        visit_cell(current_cell[0] - 2, current_cell[1] + 1, n, 'UR', current_cell, visited, bfs_queue)
        if current_cell[0] - 2 == i_end and current_cell[1] + 1 == j_end:
            destination_reached = 1
            break

        visit_cell(current_cell[0], current_cell[1] + 2, n, 'R', current_cell, visited, bfs_queue)
        if current_cell[0] == i_end and current_cell[1] + 2 == j_end:
            destination_reached = 1
            break

        visit_cell(current_cell[0] + 2, current_cell[1] + 1, n, 'LR', current_cell, visited, bfs_queue)
        if current_cell[0] + 2 == i_end and current_cell[1] + 1 == j_end:
            destination_reached = 1
            break

        visit_cell(current_cell[0] + 2, current_cell[1] - 1, n, 'LL', current_cell, visited, bfs_queue)
        if current_cell[0] + 2 == i_end and current_cell[1] - 1 == j_end:
            destination_reached = 1
            break

        visit_cell(current_cell[0], current_cell[1] - 2, n, 'L', current_cell, visited, bfs_queue)
        if current_cell[0] == i_end and current_cell[1] - 2 == j_end:
            destination_reached = 1
            break

    if destination_reached:
        pprint(visited)
        cell_info = visited[get_cell_id(i_end, j_end)]
        path = []
        moves_count = 0
        while cell_info['parent_cell'] is not None and (cell_info['cell'] != start_cell[0] or cell_info['cell'][1] != start_cell[1]):
            path.append(cell_info['move'])
            moves_count += 1
            parent_cell_id = get_cell_id(cell_info['parent_cell'][0], cell_info['parent_cell'][1])
            cell_info = visited[parent_cell_id]

        print(moves_count)
        path.reverse()
        print(*path, sep=' ')

    else:
        print('Impossible')


def visit_cell(i: int, j: int, n: int, child_pos_str: str, parent_cell: dict, visited: dict, bfs_queue: queue.Queue):
    if 0 <= i < n and 0 <= j < n:
        cell_id = get_cell_id(i, j)
        if not visited.get(cell_id):
            cell = [i, j]
            bfs_queue.put(cell)
            visited[cell_id] = {'cell': cell, 'parent_cell': parent_cell, 'move': child_pos_str}


# Use Cantor pairing function to generate unique id from two points.
def get_cell_id(i, j):
    return round((1/2 * (i + j) * (i + j + 1)) + i, 2)

if __name__ == '__main__':
    file_path = '/home/aref/Code/practice_python/problems/search/red_knights_shortest_path/input.txt'
    file = open(file_path, 'r')
    file_content = file.read()
    rows = file_content.split('\n')
    n = int(rows[0])

    i_startJ_start = rows[1].split()

    i_start = int(i_startJ_start[0])

    j_start = int(i_startJ_start[1])

    i_end = int(i_startJ_start[2])

    j_end = int(i_startJ_start[3])

    printShortestPath(n, i_start, j_start, i_end, j_end)
