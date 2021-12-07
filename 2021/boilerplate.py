def part1(data):
    return data


def part2(data):
    return data


if __name__ == "__main__":
    with open('data/day00.txt') as file:
        lines = [line for line in file.readlines()]

    print(f'Part 1: {part1(lines)}')
    print(f'Part 2: {part2(lines)}')
