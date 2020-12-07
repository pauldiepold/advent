def run_program(p_input, input):
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
            p[p[i + 1]] = input
            i += 2
        elif op == 4:
            print(get_data(p, p1, i + 1))
            i += 2
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


with open('./data/day05.txt') as file:
    program = [int(position) for position in file.read().split(',')]

run_program(program, 1)
run_program(program, 5)
