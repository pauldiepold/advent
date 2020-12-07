from itertools import permutations


def run_program(p_input, input1, input2):
    p = p_input[:]
    i = 0

    while p[i] != 99:

        instruction = str(p[i]).rjust(5, '0')
        op = int(instruction[-2:])
        p1, p2, p3 = map(int, instruction[-3:-6:-1])

        if op == 1:
            p[p[i + 3]] = get_data(p, p1, i + 1) + get_data(p, p2, i + 2)
            i += 4
        elif op == 2:
            p[p[i + 3]] = get_data(p, p1, i + 1) * get_data(p, p2, i + 2)
            i += 4
        elif op == 3:
            if input1 != 'phase_set':
                p[p[i + 1]] = input1
                input1 = 'phase_set'
            else:
                p[p[i + 1]] = input2
            i += 2
        elif op == 4:
            return get_data(p, p1, i + 1)
        elif op == 5:
            if get_data(p, p1, i + 1) != 0:
                i = get_data(p, p2, i + 2)
            else:
                i += 3
        elif op == 6:
            if get_data(p, p1, i + 1) == 0:
                i = get_data(p, p2, i + 2)
            else:
                i += 3
        elif op == 7:
            p[p[i + 3]] = int(get_data(p, p1, i + 1) < get_data(p, p2, i + 2))
            i += 4
        elif op == 8:
            p[p[i + 3]] = int(get_data(p, p1, i + 1) == get_data(p, p2, i + 2))
            i += 4


def get_data(p, mode, index):
    if mode == 0:
        return p[p[index]]
    elif mode == 1:
        return p[index]


with open('./data/day07.txt') as file:
    program = [int(position) for position in file.read().split(',')]

max_output = 0
for permutation in permutations([0, 1, 2, 3, 4], 5):
    output = 0
    for phase in range(5):
        output = run_program(program, permutation[phase], output)
        max_output = output if output > max_output else max_output
print(max_output)
