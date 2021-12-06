import numpy as np


def fish(timers, days):
    for i in range(days):
        timers = timers[1:7] + [timers[0] + timers[7]] + [timers[8]] + [timers[0]]

    return sum(timers)


if __name__ == "__main__":
    with open('data/day06.txt') as file:
        input_state = np.bincount(np.array([int(c) for c in file.readline().split(',')]))

    initial_timers = [0] * 10
    initial_timers[:6] = input_state

    print(f'Part 1: {fish(initial_timers.copy(), 80)}')
    print(f'Part 2: {fish(initial_timers.copy(), 256)}')
