def bitmask(input, mask):
    input = list('{0:036b}'.format(input))
    print("".join(input), int("".join(input), 2))
    print(mask)
    for idx, bit in enumerate(mask):
        if bit != 'X':
            input[idx] = bit
    print("".join(input), int("".join(input), 2))
    print('')
    return int("".join(input), 2)


with open('data/day14.txt') as file:
    lines = file.read().split('\n')

memory = {}
for line in lines:
    if line[:4] == 'mask':
        mask = line[-36:]
    elif line[:3] == 'mem':
        current = [int(c) for c in line.replace('mem[', '').replace(']', '').replace('= ', '').split(' ')]
        memory[current[0]] = bitmask(current[1], mask)

result = 0
for item in memory.values():
    result += item

print('Teil 1:', result)
