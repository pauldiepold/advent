import numpy as np

with open('data/day03.txt') as file:
    lines = np.array([[int(bit) for bit in line] for line in file.readlines()])

gamma = []
epsilon = []

for bit in range(len(lines[0, :])):
    count = np.bincount(lines[:, bit])
    gamma.append(np.argmax(count))
    epsilon.append(np.argmin(count))


def bin2int(binary: list):
    return int("".join(str(x) for x in binary), 2)


print(f'Part 1: {bin2int(gamma) * bin2int(epsilon)}')

oxygen_list = lines.copy()


def use_bit_criteria(numbers, type):
    for bit in range(len(lines[0, :])):
        bincount = np.bincount(numbers[:, bit])
        if type == 'oxygen':
            if bincount[0] == bincount[1]:
                criteria = 1
            else:
                criteria = np.argmax(bincount)
        else:
            if bincount[0] == bincount[1]:
                criteria = 0
            else:
                criteria = np.argmin(bincount)
        numbers = numbers[np.in1d(numbers[:, bit], criteria)]

        if len(numbers) == 1:
            return numbers[0]


oxygen_rating = bin2int(use_bit_criteria(lines.copy(), "oxygen"))
co2_rating = bin2int(use_bit_criteria(lines.copy(), "co2"))
print(f'Part 2: {oxygen_rating * co2_rating}')
