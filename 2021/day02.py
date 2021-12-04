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
    command, x = line
    result1 += directions[command] * x

    if command == 'down':
        aim += x
    if command == 'up':
        aim -= line[1]
    if command == 'forward':
        result2 += complex(x, aim * x)

print(f'Part 1: {int(result1.real * result1.imag)}')
print(f'Part 2: {int(result2.real * result2.imag)}')
