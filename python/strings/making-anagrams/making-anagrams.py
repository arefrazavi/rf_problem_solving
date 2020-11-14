#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict


# Calculate number of occurance of each character in given string.
def get_char_freqs(input_str):
    char_freqs = defaultdict(lambda: 0)
    for char in input_str:
        char_freqs[char] += 1

    return char_freqs


# Complete the makeAnagram function below.
def makeAnagram(a, b):
    intersection_count = 0
    a_char_freqs = get_char_freqs(a)
    b_char_freqs = get_char_freqs(b)

    # Find number of common characters between two strings.
    for char, char_freq in a_char_freqs.items():
        if b_char_freqs.get(char):
            intersection_count += min(a_char_freqs[char], b_char_freqs[char])

    deleted_chars_count = len(a) + len(b) - 2 * intersection_count

    return deleted_chars_count


if __name__ == '__main__':
    file_path = 'input'
    file = open(file_path, 'r')
    file_content = file.read()
    rows = file_content.split('\n')
    a = rows[0]
    b = rows[1]
    print(makeAnagram(a, b))
