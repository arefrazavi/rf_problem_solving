
def countPairs(arr):
    pow_two_count = 0
    arr_len = len(arr)
    for i in range(arr_len-1):
        for j in range(i+1, arr_len):
            if is_pow_of_two(arr[i] & arr[j]):
                pow_two_count += 1
    return pow_two_count


