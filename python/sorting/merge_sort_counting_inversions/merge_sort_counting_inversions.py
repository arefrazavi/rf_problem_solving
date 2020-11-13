# https://www.hackerrank.com/challenges/ctci-merge-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

# !/bin/python3

import math
import os
import random
import re
import sys


def merge_and_count_inversion(arr1, arr2):
    i = 0
    j = 0
    arr1_len = len(arr1)
    arr2_len = len(arr2)

    arr = []
    inversion_count = 0
    while i < arr1_len and j < arr2_len:
        if arr1[i] > arr2[j]:
            # when arr1[i] > arr2[j], arr1[j] is lower than every element after i in arr1 too,
            # so it must be swapped with all of them.
            inversion_count += arr1_len - i
            arr.append(arr2[j])
            j += 1
        else:
            arr.append(arr1[i])
            i += 1

    while i < arr1_len:
        arr.append(arr1[i])
        i += 1

    while j < arr2_len:
        arr.append(arr2[j])
        j += 1

    return (arr, inversion_count)


def merge_sort_count_inversions(arr):
    arr_len = len(arr)
    if arr_len == 1:
        return arr, 0
    mid_index = arr_len // 2

    (arr1, inversion_count_1) = merge_sort_count_inversions(arr[0:mid_index])
    (arr2, inversion_count_2) = merge_sort_count_inversions(arr[mid_index:])

    (arr, inversion_count_3) = merge_and_count_inversion(arr1, arr2)

    inversion_count = inversion_count_1 + inversion_count_2 + inversion_count_3

    return (arr, inversion_count)


# Complete the countInversions function below.
def countInversions(arr):
    (arr, inversion_count) = merge_sort_count_inversions(arr)

    print(tuple(arr))
    return inversion_count


file_path = 'input'
file = open(file_path, 'r')
file_content = file.read()
rows = file_content.split('\n')
t = int(rows.pop(0))

for t_itr in range(t):
    n = int(rows.pop(0))

    arr = list(map(int, rows.pop(0).rstrip().split()))

    result = countInversions(arr)

    print(result)
