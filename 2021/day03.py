import numpy as np

with open('data/day03.txt') as file:
    lines = np.array([[int(bit) for bit in line] for line in file.read().split('\n')])

gamma = []
epsilon = []

for bit in range(len(lines[0, :])):
    count = np.bincount(lines[:, bit])
    gamma.append(np.argmax(count))
    epsilon.append(np.argmin(count))


def bin2int(binary: list):
    return int("".join(str(x) for x in binary), 2)


gamma = bin2int(gamma)
epsilon = bin2int(epsilon)

print(f'Part 1: {gamma * epsilon}')
