#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'processLogs' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY logs
#  2. INTEGER threshold
#
from pprint import pprint


def processLogs(logs, threshold):
    transaction_counts = {}
    for log in logs:
        (sender_id, receiver_id, amount) = log.split()

        if transaction_counts.get(sender_id):
            transaction_counts[sender_id] += 1
        else:
            transaction_counts[sender_id] = 1

        if int(sender_id) != int(receiver_id):
            if transaction_counts.get(receiver_id):
                transaction_counts[receiver_id] += 1
            else:
                transaction_counts[receiver_id] = 1

    abusive_users = []
    for user_id, transaction_count in transaction_counts.items():
        if transaction_count >= threshold:
            abusive_users.append(user_id)

    abusive_users.sort(key = int)

    return abusive_users


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    logs_count = int(input().strip())

    logs = []

    for _ in range(logs_count):
        logs_item = input()
        logs.append(logs_item)

    threshold = int(input().strip())

    result = processLogs(logs, threshold)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
