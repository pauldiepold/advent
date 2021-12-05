with open('data/day01.txt') as file:
    lines = [int(x) for x in file.readlines()]

result1 = 0
result2 = 0

for index, measurement in enumerate(lines):
    if index != 0 and measurement > lines[index - 1]:
        result1 += 1

    if index not in [0, 1, 2] and sum(lines[index - 3:index - 0]) < sum(lines[index - 2:index + 1]):
        result2 += 1

print(f'Teil 1: {result1}')
print(f'Teil 2: {result2}')
