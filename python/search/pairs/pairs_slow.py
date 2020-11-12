#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(difference, arr):
    arr = sorted(arr)
    arr_len = len(arr)

    difference_count = 0
    for i in range(arr_len-1):
        j = i + 1
        while j < arr_len and (arr[j] - arr[i]) <= difference:
            if arr[j] - arr[i] == difference:
                difference_count += 1
            j += 1

    return difference_count


file_path = '/problems/search/input.txt'
file = open(file_path, 'r')
file_content = file.read()
rows = file_content.split('\n')

nk = rows[0].split()
n = int(nk[0])
k = int(nk[1])
arr = list(map(int, rows[1].rstrip().split()))
pairs_count = pairs(k, arr)

print(pairs_count)
