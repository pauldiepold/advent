import numpy as np

with open('data/day11.txt') as file:
    inp = np.array([[int(position == '.') for position in row] for row in file.read().split('\n')])

n = inp.shape[0] if inp.shape[0] >= inp.shape[1] else inp.shape[1]
floor = np.ones((n, n))
floor[:inp.shape[0], :inp.shape[1]] = inp

R = (np.eye(n) + np.eye(n, n, 1) + np.eye(n, n, -1))
seats = np.zeros((n, n))
seats_old = np.ones((n, n))

while not np.array_equal(seats, seats_old):
    neighbors = np.dot(np.dot(R, seats), R) - seats
    seats_old = seats
    seats = (((neighbors == 0) | ((seats == 1) & (neighbors < 4))) & (floor == 0)).astype(np.int)

print('Teil 1:', np.sum(seats))
