#!/bin/python3

import os
from collections import defaultdict, Counter


def get_mode(arr):
    items_count = Counter(arr)
    return items_count.most_common(1)[0][0]


# Complete the isValid function below.
def isValid(string):
    chars_freq = defaultdict(lambda: 0)
    # Enumerate frequency of every character in the given string.
    for char in string:
        chars_freq[char] += 1

    # Find the most freqent number of the occurance of characters.
    freq_mode = get_mode(chars_freq.values())
    min_allowed_remove = 1
    remove_count = 0
    is_valid = 'YES'
    # Check how many characters must be removed to make the string valid.
    for char_freq in chars_freq.values():
        if char_freq == freq_mode:
            continue
        elif char_freq < freq_mode:
            remove_count += char_freq
        else:
            remove_count += char_freq - freq_mode

        # If the number of removal is more than the minimum allowed (1),
        # string is invalid.
        if remove_count > min_allowed_remove:
            is_valid = 'NO'
            break

    return is_valid


if __name__ == '__main__':
    file_path = 'input'
    file = open(file_path, 'r')
    string = file.read()
    print(isValid(string))
