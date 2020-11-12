#!/bin/python3

import os
import sys

from pprint import pprint


def convert_constraint_list_to_dic(constraint_list):
    constraint_dict = {}
    for i in constraint_list:
        constraint_dict[i] = 1

    return constraint_dict


#
# Complete the extremumPermutations function below.
#
def count_permutation(n):
    perm_count = {1: {1: 1}}

    for i in range(2, n + 1):
        perm_count[i] = {}
        j = i
        while j > 0:
            perm_count[i][j] = sum(perm_count[i - 1].values())
            j -= 1

    #pprint(perm_count)
    return sum(perm_count[n].values())

file_path = '/home/aref/Code/practice_python/problems/dynamic_programming/extremum_permutations/input.txt'
file = open(file_path, 'r')
file_content = file.read()
n = int(input())
result = count_permutation(n)

print(result)
