import cmath

directions = {
    'forward': complex(1, 0),
    'down': complex(0, 1),
    'up': complex(0, -1)
}

result1 = complex(0, 0)
result2 = complex(0, 0)
aim = 0

with open('data/day02.txt') as file:
    lines = [[x.split(' ')[0], int(x.split(' ')[1])] for x in file.read().split('\n')]

for line in lines:
    result1 += directions[line[0]] * line[1]

    if line[0] == 'down':
        aim += line[1]
    if line[0] == 'up':
        aim -= line[1]
    if line[0] == 'forward':
        result2 += complex(line[1], aim * line[1])

print(f'Part 1: {int(result1.real * result1.imag)}')
print(f'Part 2: {int(result2.real * result2.imag)}')
