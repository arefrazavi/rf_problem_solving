# https://www.youtube.com/watch?v=mjZpZ_wcYFg
# aaaabbcccca => 4a2b3c1a
# https://www.geeksforgeeks.org/stack-in-python/

from collections import deque


# Use iterative approach to solve the problem.
# stack (LIFO) data structure to encode since order matters
def encode_by_run_length(raw_str: str) -> str:
    # Input validation
    if not raw_str.rstrip():
        return ''

    char_stack = deque([raw_str[0]])
    encoded_str = ''
    pre_char_count = 1
    raw_str_len = len(raw_str)
    for i in range(1, raw_str_len + 1):
        if i >= raw_str_len or raw_str[i] != raw_str[i - 1]:
            # pre_char_count = 0
            # while char_stack:
            #     char_stack.pop()
            #      pre_char_count += 1
            encoded_str += str(pre_char_count) + raw_str[i - 1]
            pre_char_count = 1
        else:
            pre_char_count += 1

        # char_stack.append(raw_str[i])

    # if char_stack:
    #     last_char = char_stack[0]
    #     pre_char_count = 0
    #     while char_stack:
    #         char_stack.pop()
    #         pre_char_count += 1
    #     encoded_str += str(pre_char_count) + last_char

    return encoded_str


input_str = input()

encoded_str = encode_by_run_length(input_str)

print(encoded_str)
