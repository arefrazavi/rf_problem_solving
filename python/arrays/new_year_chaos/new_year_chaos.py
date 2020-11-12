#!/bin/python3

import math
import os
import random
import re
import sys

MIN_BRIBES_PER_PERSON = 2

# Complete the minimumBribes function below.
def minimumBribes(person_queue):
    total_bribes_count = 0
    person_queue_len = len(person_queue)

    for i in range(person_queue_len - 2, -1, -1):
        person_bribes_count = 0
        j = i
        # Place the person to in its original sorted order and count its swapes.
        # Number of swaps indicated the minimum number bribes dones by person.
        while j < (person_queue_len - 1) and person_queue[j+1] < person_queue[j]:
            temp = person_queue[j+1]
            person_queue[j+1] = person_queue[j]
            person_queue[j] = temp
            person_bribes_count +=1
            j += 1

        if person_bribes_count > MIN_BRIBES_PER_PERSON:
            return 'Too chaotic'

        total_bribes_count += person_bribes_count

    return total_bribes_count



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
