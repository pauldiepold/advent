def fish(timers, days):
    for i in range(days):
        timers[:] = timers[1:7] + [timers[0] + timers[7]] + [timers[8]] + [timers[0]]

    return sum(timers)


if __name__ == "__main__":
    with open('data/day06.txt') as file:
        initial_states = [int(c) for c in file.readline().split(',')]

    initial_timers = [initial_states.count(i) for i in range(9)]

    print(f'Part 1: {fish(initial_timers, 80)}')
    print(f'Part 2: {fish(initial_timers, 256 - 80)}')
