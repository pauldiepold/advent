import numpy as np

with open('data/day05.txt') as file:
    lines = np.array([[[int(c) for c in y.split(',')] for y in line.split(' -> ')] for line in file.readlines()])

coords1 = np.zeros((np.max(lines[:, :, 0]) + 1, np.max(lines[:, :, 1]) + 1))
coords2 = np.copy(coords1)

for line in lines:
    x1, y1, x2, y2 = line.flatten()

    # Part 1
    if x1 == x2 or y1 == y2:
        coords1[min(x1, x2):max(x1, x2) + 1, min(y1, y2):max(y1, y2) + 1] += 1

    # Part 2
    x_dir, y_dir = np.sign([x2 - x1, y2 - y1])
    for n in range(max(abs(x2 - x1), abs(y2 - y1)) + 1):
        coords2[x1 + n * x_dir, y1 + n * y_dir] += 1

print(f'Part 1:  {np.count_nonzero(coords1 > 1)}')
print(f'Part 2:  {np.count_nonzero(coords2 > 1)}')
