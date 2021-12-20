import math
from itertools import permutations


def reduction(number):
    reduced = True
    while reduced:
        depth = 0
        reduced = False
        exploded = False
        for i in range(len(number)):
            c = number[i]
            if c == '[':
                if depth == 4:
                    number = explode(number, i)
                    reduced = True
                    exploded = True
                    break
                else:
                    depth += 1
            elif c == ']':
                depth -= 1
        if not exploded:
            for i in range(len(number)):
                c = number[i]
                if isinstance(c, int) and c > 9:
                    number = split(number, i)
                    reduced = True
                    break
    return number


def split(number, i):
    # print_list(number)
    # print('-' * i + "^   split")
    to_split = number[i]
    left = int(to_split / 2)
    right = math.ceil(to_split / 2)
    number = number[:i] + ['['] + [left] + [','] + [right] + [']'] + number[i + 1:]
    return number


def explode(number, i):
    # if number[i + 2] != ',' and number[i] != '[' and number[i + 4] != ']':
    #     print('next explode')
    #     return explode(number, i + 1)
    # print_list(number)
    # print('-' * i + "^   explode")
    left = number[i + 1]
    right = number[i + 3]
    for n in range(i - 1, -1, -1):
        if isinstance(number[n], int):
            number[n] += left
            break
    for n in range(i + 4, len(number)):
        if isinstance(number[n], int):
            number[n] += right
            break
    number[i] = 0
    for _ in range(4):
        number.pop(i + 1)
    return number


def print_list(string_list):
    print(''.join([str(c) for c in string_list]))


def calc_mag(number):
    found_pair = True
    while found_pair:
        found_pair = False
        for i in range(len(number)):
            if number[i] == '[' and number[i + 2] == ',' and number[i + 4] == ']':
                left = number[i + 1]
                right = number[i + 3]
                number[i] = 3 * left + 2 * right
                for _ in range(4):
                    number.pop(i + 1)
                found_pair = True
                break
    # print(len(number))
    return number[0]


if __name__ == "__main__":
    with open('data/day18.txt') as file:
        lines = [[int(c) if c.isnumeric() else c for c in line] for line in file.read().split('\n')]

    result = lines[0]

    for line in lines[1:]:
        # print_list(result)
        # print('+')
        # print_list(line)
        # print('----------- Start of reduction -----------')
        result = ['['] + result + [','] + line + [']']
        result = reduction(result)
        # print('----------- End of reduction -----------')
        # print_list(result)

    print(calc_mag(result))

    max_mag = 0
    for first, second in permutations(lines, 2):
        addition = ['['] + first + [','] + second + [']']
        mag = calc_mag(reduction(addition))
        if mag > max_mag:
            max_mag = mag
    print(max_mag)
