# https://www.hackerrank.com/challenges/s10-basic-statistics/problem
from collections import defaultdict

def get_mean(numbers, n):
    return round(sum(numbers)/n, 1)

def get_median(numbers, n):
    numbers = sorted(numbers)
    if n % 2 == 0:
        median = round((numbers[(n-1)//2] + numbers[n//2]) / 2, 1)
    else:
        median = numbers[n//2]

    return median

def get_mode(numbers, n):
    number_counts = defaultdict(lambda: 0)

    for number in numbers:
        number_counts[number] += 1

    max_count = -1
    mode = number_counts[numbers[0]]
    for number, count in number_counts.items():
        if count > max_count:
            max_count = count
            mode = number
        elif count == max_count and number < mode:
            max_count = count
            mode = number

    return mode


n = int(input())

numbers = list(map(int, input().rstrip().split()))

print(get_mean(numbers, n))
print(get_median(numbers, n))
print(get_mode(numbers, n))
