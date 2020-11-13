# didn't resolve the timeout :(

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
def extremumPermutations(n, a, b):
    a_dict = convert_constraint_list_to_dic(a)
    b_dict = convert_constraint_list_to_dic(b)
    # pprint(a_dict)
    # pprint(b_dict)
    perm_count = {1: {1: 1}}
    sum_count = {1: 1}
    for i in range(2, n + 1):
        perm_count[i] = {}
        sum_count[i] = 0
        j = i
        if (a_dict.get(i) and b_dict.get(i)) or (a_dict.get(i) and a_dict.get(i-1)) or (b_dict.get(i) and b_dict.get(i-1)):
            return 0
        while j > 0:
            perm_count[i][j] = 0
            if a_dict.get(i) or b_dict.get(i - 1):
                if i > j:
                    if perm_count[i - 1][j] == perm_count[i - 1][i-1]:
                        perm_count[i][j] = ((i - j) * perm_count[i - 1][j]) % 1000000007
                    else:
                        for k in range(j, i):
                            perm_count[i][j] += perm_count[i - 1][k]
            elif a_dict.get(i - 1) or b_dict.get(i):
                if j > 1:
                    if perm_count[i - 1][1] == perm_count[i - 1][j-1]:
                        perm_count[i][j] = ((j - 1) * perm_count[i - 1][1]) % 1000000007
                    else:
                        for k in range(1, j):
                            perm_count[i][j] += perm_count[i - 1][k]
            else:
                perm_count[i][j] = sum_count[i - 1] % 1000000007
            sum_count[i] += perm_count[i][j]
            j -= 1

    return sum_count[n] % 1000000007


file_path = 'input'
file = open(file_path, 'r')
file_content = file.read()
rows = file_content.split('\n')

nkl = rows[0].split()
n = int(nkl[0])
k = int(nkl[1])
l = int(nkl[2])

a = list(map(int, rows[1].rstrip().split()))

b = list(map(int, rows[2].rstrip().split()))

result = extremumPermutations(n, a, b)

print(result)
