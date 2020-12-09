from itertools import combinations

with open('./data/day09.txt') as file:
    numbers = [int(number) for number in file.read().split('\n')]

for i in range(25, len(numbers)):
    sum_found = False
    for combination in combinations(numbers[i - 25:i], 2):
        if sum(combination) == numbers[i]:
            sum_found = True
            break
    if not sum_found:
        sum_found = numbers[i]
        print('Teil 1:', sum_found)
        break

for k in range(len(numbers)):
    contiguous_range = []
    for j in range(k, len(numbers)):
        contiguous_range.append(numbers[j])
        if sum(contiguous_range) == sum_found:
            print('Teil 2:', min(contiguous_range) + max(contiguous_range))
            break
