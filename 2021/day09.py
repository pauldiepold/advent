import numpy as np


def part1(tubes):
    size = tubes.shape
    result = 0
    lows = []
    for x in range(size[0]):
        for y in range(size[1]):
            is_low = True
            n = tubes[x, y]
            if x != 0 and n >= tubes[x - 1, y]:
                is_low = False
            if x != size[0] - 1 and n >= tubes[x + 1, y]:
                is_low = False
            if y != 0 and n >= tubes[x, y - 1]:
                is_low = False
            if y != size[1] - 1 and n >= tubes[x, y + 1]:
                is_low = False
            if is_low:
                result += 1 + tubes[x, y]
                lows.append((x, y))

    return result, lows


def part2(tubes, lows):
    def search_for_basin(basin, x, y):
        n = tubes[x, y]
        if n != 9 and (x, y) not in basin:
            basin.append((x, y))
            if x != 0 and n < tubes[x - 1, y]:
                search_for_basin(basin, x - 1, y)
            if x != size[0] - 1 and n < tubes[x + 1, y]:
                search_for_basin(basin, x + 1, y)
            if y != 0 and n < tubes[x, y - 1]:
                search_for_basin(basin, x, y - 1)
            if y != size[1] - 1 and n < tubes[x, y + 1]:
                search_for_basin(basin, x, y + 1)

    basins = []
    size = tubes.shape

    for low in lows:
        curr_basin = []
        search_for_basin(curr_basin, *low)
        basins.append(len(curr_basin))
    biggest_basins = sorted(basins)[-3:]

    return biggest_basins[0] * biggest_basins[1] * biggest_basins[2]


if __name__ == "__main__":
    with open('data/day09.txt') as file:
        lines = np.array([[int(x) for x in line] for line in file.read().split('\n')])

    result1, low_points = part1(lines)

    print(f'Part 1: {result1}')
    print(f'Part 2: {part2(lines, low_points)}')
