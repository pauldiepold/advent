from collections import Counter

with open('./data/day10.txt') as file:
    numbers = [int(number) for number in file.read().split('\n')]

numbers.append(0)
numbers.append(max(numbers) + 3)
numbers.sort()
diffs = [numbers[i] - numbers[i - 1] for i in range(1, len(numbers))]
count = Counter(diffs)

print('Teil 1:', count[1] * count[3])


def combinations(ones):
    n = ones - 1
    if ones <= 1:
        return 1
    elif ones > 1:
        return 2 ** n - sum([2 ** i for i in range(0, n - 3 + 1)])


ones = 0
result = 1
for idx, diff in enumerate(diffs):
    if diff == 1:
        ones += 1
    elif diff == 3 or idx == len(diffs) - 1:
        result *= combinations(ones)
        ones = 0

print('Teil 2:', result)
