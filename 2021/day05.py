import numpy as np

with open('data/day05.txt') as file:
    lines = np.array([[[int(c) for c in y.split(',')] for y in line.split(' -> ')] for line in file.read().split('\n')])

coords = np.zeros((np.max(lines[:, :, 0]), np.max(lines[:, :, 1])))

for line in lines:
    x1, y1 = line[0]
    x2, y2 = line[1]
    if x1 == x2 or y1 == y2:
        x_min = min(x1, x2)
        x_max = max(x1, x2)
        y_min = min(y1, y2)
        y_max = max(y1, y2)
        coords[x_min:x_max + 1, y_min:y_max + 1] += 1

print(f'Part 1:  {np.count_nonzero(coords > 1)}')
