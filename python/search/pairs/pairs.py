# https://www.hackerrank.com/challenges/pairs/problem

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(difference, arr):
    difference_count = 0
    # Skip duplicate elements because we want to count distinct pairs
    arr = set(arr)
    for i in arr:
        if i+difference in arr:
            difference_count += 1

    return difference_count


file_path = '/problems/search/pairs/input.txt'
file = open(file_path, 'r')
file_content = file.read()
rows = file_content.split('\n')

nk = rows[0].split()
n = int(nk[0])
k = int(nk[1])
arr = list(map(int, rows[1].rstrip().split()))
pairs_count = pairs(k, arr)

print(pairs_count)
