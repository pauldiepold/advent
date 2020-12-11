import numpy as np

with open('./data/day11.txt') as file:
    floor_input = np.array([[int(position == '.') for position in row] for row in file.read().split('\n')]).astype(
        np.int)

n_input = floor_input.shape[0]
m_input = floor_input.shape[1]

n = n_input if n_input >= m_input else m_input
floor = np.ones((n, n)).astype(np.int)
floor[:n_input, :m_input] = floor_input

R = (np.eye(n) + np.eye(n, n, 1) + np.eye(n, n, -1)).astype(np.int)
seats = np.zeros(n).astype(np.int)
seats_old = np.random.rand(n, n)

while not np.array_equal(seats, seats_old):
    neighbors = np.dot(np.dot(R, seats), R) - seats
    seats_old = seats
    seats = (((neighbors == 0) | ((seats == 1) & (neighbors < 4))) & (floor == 0)).astype(np.int)

print('Teil 1:', np.sum(seats))
