#
# Complete the 'countGroups' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING_ARRAY related as parameter.
#
from pprint import pprint


def countGroups(related_sub_mat):
    related_groups = []
    visited = {}
    sub_len = len(related_sub_mat)
    for i in range(sub_len):
        if not visited.get(i):
            sub_relatives = [i]
            explore_sub(i, related_sub_mat, sub_len, sub_relatives, visited)
            # pprint(node_related_list)
            related_groups.append(sub_relatives)

    return len(related_groups)


def explore_sub(i, related_sub_mat, sub_len, sub_relatives, visited):
    visited[i] = True
    for j in range(sub_len):
        # print(related_mat[i][j])
        if related_sub_mat[i][j] == '1' and i != j:
            # print (str(j) + ' related to ' + str(i))
            sub_relatives.append(j)
            if not visited.get(j):
                explore_sub(j, related_sub_mat, sub_len, sub_relatives, visited)


if __name__ == '__main__':
    pass
