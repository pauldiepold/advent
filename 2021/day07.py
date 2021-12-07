def part1(crabs):
    median = sorted(crabs)[int(len(crabs) / 2) - 1]

    return sum([abs(crab - median) for crab in crabs])


def part2(crabs):
    mean = int(sum(crabs) / len(crabs))

    return sum([extra_fuel(abs(crab - mean)) for crab in crabs])


def extra_fuel(distance):
    return sum([i for i in range(1, distance + 1)])


if __name__ == "__main__":
    with open('data/day07.txt') as file:
        d = [int(c) for c in file.readline().split(',')]

    print(f'Part 1: {part1(d)}')
    print(f'Part 2: {part2(d)}')
