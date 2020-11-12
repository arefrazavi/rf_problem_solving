#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maximumToys function below.
def maximumToys(prices, budget):
    prices = sorted(prices)
    expenditure = 0
    max_toys_count = 0
    for price in prices:
        if (expenditure + price) <= budget:
            expenditure += price
            max_toys_count += 1

    return max_toys_count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()
