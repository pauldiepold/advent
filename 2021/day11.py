import numpy as np


def octopussies(energy):
    e = np.eye(energy.shape[0], energy.shape[1] + 1)
    r = np.eye(*energy.shape) + e[:, 1:] + np.transpose(e[:, 1:])
    result1, result2 = 0, 0

    for n in range(99999):
        flashed = np.zeros(energy.shape)
        energy += 1
        while True:
            flashes = (energy > 9) - flashed
            flashed += flashes
            if not flashes.any():
                break
            increments = r @ flashes @ r - flashes
            energy += increments

        energy[flashed != 0] = 0

        if n < 100:
            result1 += np.count_nonzero(flashed)

        if flashed.all():
            result2 = n + 1
            break

    return result1, result2


if __name__ == "__main__":
    with open('data/day11.txt') as file:
        lines = np.array([[float(x) for x in line] for line in file.read().split('\n')])

    print(octopussies(lines))
