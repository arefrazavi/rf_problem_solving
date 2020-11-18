# Enter your code here. Read input from STDIN. Print output to STDOUT


def calculate_standard_deviation(numbers):
    n = len(numbers)
    mean = sum(numbers) / n
    # Sum of squared distance of each number from the mean.
    squared_distance_sum = 0
    for number in numbers:
        squared_distance_sum += (number - mean) ** 2

    standard_deviation = (squared_distance_sum / n) ** (1 / 2)

    return round(standard_deviation, 1)


n = int(input())

numbers = list(map(int, input().rstrip().split()))

print(calculate_standard_deviation(numbers))
