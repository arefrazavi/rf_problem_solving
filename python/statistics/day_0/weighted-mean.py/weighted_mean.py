# Enter your code here. Read input from STDIN. Print output to STDOUT


def cal_weighted_mean(numbers, weights):
    mean = 0

    for i in range(len(numbers)):
        mean += numbers[i] * weights[i]
    mean /= sum(weights)

    return round(mean, 1)


n = input()
numbers = list(map(int, input().rstrip().split()))
weights = list(map(int, input().rstrip().split()))

weighted_mean = cal_weighted_mean(numbers, weights)

print(weighted_mean)

