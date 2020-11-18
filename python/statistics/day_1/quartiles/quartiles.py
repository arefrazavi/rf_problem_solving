# Enter your code here. Read input from STDIN. Print output to STDOUT

def calculate_median_by_range(numbers, start_index, end_index):
    range_len = end_index - start_index + 1
    median_index = (end_index + start_index) // 2
    if range_len % 2 == 0:
        return (numbers[median_index] + numbers[median_index + 1]) / 2
    else:
        return numbers[median_index]


def calculate_quartiles(numbers: list):
    numbers.sort()
    numbers_len = len(numbers)
    start_index = 0
    end_index = numbers_len - 1
    mid_index = end_index // 2
    quartiles = {}
    quartiles['q2'] = calculate_median_by_range(numbers, start_index, end_index)
    quartiles['q3'] = calculate_median_by_range(numbers, mid_index + 1, end_index)
    if numbers_len % 2 == 0:
        quartiles['q1'] = calculate_median_by_range(numbers, start_index, mid_index)
    else:
        quartiles['q1'] = calculate_median_by_range(numbers, start_index, mid_index - 1)

    print(int(quartiles['q1']))
    print(int(quartiles['q2']))
    print(int(quartiles['q3']))


n = int(input())
numbers = list(map(int, input().rstrip().split()))

calculate_quartiles(numbers)
