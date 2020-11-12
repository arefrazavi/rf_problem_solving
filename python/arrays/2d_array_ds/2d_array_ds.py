#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def cal_hourglass_sum_max(arr):
    arr_len = len(arr)
    hourglass_sums = []
    for i in range(arr_len):
        if (i + 3) > arr_len:
            continue
        for j in range(arr_len):
            if (j + 3) > arr_len:
                continue
            hourglass_sum = sum(arr[i][j:j+3]) + arr[i+1][j+1] + sum(arr[i+2][j:j+3])
            hourglass_sums.append(hourglass_sum)

    return max(hourglass_sums)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = cal_hourglass_sum_max(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
