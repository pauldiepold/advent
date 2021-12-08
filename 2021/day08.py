def part1(data):
    return len([output for display in data for output in display[1] if len(output) in [2, 3, 4, 7]])


def part2(data):
    result = 0

    for display in data:
        patterns, codes = display
        decoded = {}
        # 1, 4, 7 und 8 sind über die Länge eindeutig zuzuordnen
        for pattern in patterns:
            unique_lengths = {2: 1, 3: 7, 4: 4, 7: 8}
            if len(pattern) in unique_lengths:
                decoded[unique_lengths[len(pattern)]] = pattern

        # alle Segmente mit Länge 6 betrachten
        for pattern in patterns:
            if len(pattern) == 6:
                # wenn 7 nicht enthalten ist --> 6
                if not all_chars_contained(decoded[7], pattern):
                    decoded[6] = pattern
                # wenn 4 nicht enthalten ist --> 9
                elif all_chars_contained(decoded[4], pattern):
                    decoded[9] = pattern
                # sonst muss es 0 sein
                else:
                    decoded[0] = pattern

        # alle Segmente mit Länge 5 betrachten
        for pattern in patterns:
            if len(pattern) == 5:
                # wenn 1 nicht enthalten ist --> 3
                if all_chars_contained(decoded[1], pattern):
                    decoded[3] = pattern
                # wenn das pattern nicht in 9 ist --> 5
                elif all_chars_contained(pattern, decoded[9]):
                    decoded[5] = pattern
                # sonst muss es 2 sein
                else:
                    decoded[2] = pattern

        decoded_inverse = {v: k for k, v in decoded.items()}

        four_digits = ''
        for code in codes:
            four_digits += str(decoded_inverse[code])

        result += int(four_digits)

    return result


def all_chars_contained(needles, haystack):
    return all([c in haystack for c in needles])


if __name__ == "__main__":
    with open('data/day08.txt') as file:
        d = [[["".join(sorted(y)) for y in x.split(' ')] for x in c.split(' | ')] for c in file.read().split('\n')]

    print(f'Part 1: {part1(d)}')
    print(f'Part 2: {part2(d)}')
