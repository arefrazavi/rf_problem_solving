#!/bin/python3

import os


# Complete the minimumSwaps function below.
# Use selection sort algorithm to count minimum of swaps
def minimumSwaps(arr):
    arr_len = len(arr)
    swaps_count = 0
    for i in range(arr_len):
        j = i
        min_index = j
        # Find the minimum element for the rest of the array and put it in its sorted position (i).
        for j in range(i + 1, arr_len):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            temp = arr[i]
            arr[i] = arr[min_index]
            arr[min_index] = temp
            swaps_count += 1

    return swaps_count


if __name__ == '__main__':
    file_path = 'input'
    file = open(file_path, 'r')
    file_content = file.read()
    rows = file_content.split('\n')
    n = int(rows[0])
    arr = list(map(int, rows[1].rstrip().split()))
    print(minimumSwaps(arr))
