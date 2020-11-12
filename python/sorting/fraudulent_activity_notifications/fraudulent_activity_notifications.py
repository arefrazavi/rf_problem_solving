import math
import os
import random
import re
import sys
from bisect import bisect_left, insort_left


def find_median(elements: list, elements_len):
    # elements_len = len(elements)
    median_base_index = int((elements_len - 1) / 2)
    if (elements_len % 2) != 0:
        median = float(elements[median_base_index])
    else:
        median = float((elements[median_base_index] + elements[median_base_index + 1]) / 2)

    return median


# Complete the activityNotifications function below.
def activityNotifications(expenditure, trailing_number):
    prior_transaction_data = sorted(expenditure[:trailing_number])
    notification_count = 0
    for day_index in range(d, len(expenditure)):
        if expenditure[day_index] >= 2 * find_median(prior_transaction_data, trailing_number):
            notification_count += 1

        # Find the oldest expenditure in prior trailing_number transactions (before day_index)
        # and remove it from sorted prior_transaction_data
        del prior_transaction_data[bisect_left(prior_transaction_data, expenditure[day_index - trailing_number])]
        # Add the current expenditure (happened in day_index) to prior_transaction_data
        # in a way that prior_transaction_data stay sorted.
        insort_left(prior_transaction_data, expenditure[day_index])
        #print(*prior_transaction_data, sep=' ')

    return notification_count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nd = input().split()
    n = int(nd[0])
    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))
    result = activityNotifications(expenditure, d)
    print(result)
    
    # fptr.write(str(result) + '\n')
    # fptr.close()
