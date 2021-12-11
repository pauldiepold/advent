import numpy as np


def octopussies(energy):
    n = len(energy)
    e = np.eye(n, n + 1)
    r = np.eye(n, n) + e[:, 1:] + e[:, 1:].T
    result1, result2 = 0, 0

    for i in range(99999):
        flashed = np.zeros((n, n))
        flashes = np.ones((n, n))
        energy += 1
        while flashes.any():
            flashes = (energy > 9) - flashed
            flashed += flashes
            increments = r @ flashes @ r - flashes
            energy += increments

        energy[flashed != 0] = 0

        if i < 100:
            result1 += np.count_nonzero(flashed)

        if flashed.all():
            result2 = i + 1
            break

    return result1, result2


if __name__ == "__main__":
    with open('data/day11.txt') as file:
        lines = np.array([[float(x) for x in line] for line in file.read().split('\n')])

    print(octopussies(lines))
