# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque

# Complete the rotLeft function below.
def rotLeft(arr, rotations):
    arr_deque = deque(arr)
    for i in range(rotations):
        # Move the first element from most left postion to the moset right position.
        old_first_element = arr_deque.popleft()
        arr_deque.append(old_first_element)

    return arr_deque

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
