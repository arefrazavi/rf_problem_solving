#!/bin/python3

import os
from pprint import pprint

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    arr_len = len(arr)

    # pos_value_arr keeps the three piece of information about every element in given arr:
    # position in sorted version, (original position, value)
    pos_value_arr = [*enumerate(arr)]
    pos_value_arr.sort(key=lambda item: item[1])

    swaps_count = 0
    visited = {}
    # Find the exlusive cycles of elements which must be swapped in order to be in their sorted postions  -> O(n)
    for i in range(arr_len):
        j = i
        # Number of edges in a cycle.
        cycle_size = 0
        while not visited.get(j) and j != pos_value_arr[j][0]:
            visited[j] = True
            # i => pos_value_arr[j][0] is one edge of the cycle.
            cycle_size += 1
            j = pos_value_arr[j][0]
        # If there is any cycle, number of swaps for the cycle is (cycle size - 1).
        if cycle_size > 0:
            swaps_count += cycle_size - 1

    return swaps_count


if __name__ == '__main__':
    file_path = 'input'
    file = open(file_path, 'r')
    file_content = file.read()
    rows = file_content.split('\n')
    n = int(rows[0])
    arr = list(map(int, rows[1].rstrip().split()))
    print(minimumSwaps(arr))