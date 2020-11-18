#
# Complete the 'countPairs' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY nodes as parameter.
#
def is_pow_of_two(number):
    return (number and (not(number & (number - 1))))


def countPairs(arr):
    pow_two_count = 0
    arr_len = len(arr)
    for i in range(arr_len-1):
        for j in range(i+1, arr_len):
            if is_pow_of_two(arr[i] & arr[j]):
                pow_two_count += 1
    return pow_two_count

