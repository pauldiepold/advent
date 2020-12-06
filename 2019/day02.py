def run_program(p_input, noun, verb):
    p = p_input[:]
    p[1] = noun
    p[2] = verb
    current = 0
    while p[current] != 99:
        if not p[current] in (1, 2):
            print('error', p[current])
            break
        if p[current] == 1:
            p[p[current + 3]] = p[p[current + 1]] + p[p[current + 2]]
        elif p[current] == 2:
            p[p[current + 3]] = p[p[current + 1]] * p[p[current + 2]]
        current += 4
    return p[0]


def find_combination():
    for i in range(0, 100):
        for j in range(0, 100):
            if run_program(program, i, j) == 19690720:
                return 100 * i + j


with open('./data/day02.txt') as file:
    program = [int(position) for position in file.read().split(',')]

print('Teil 1:', run_program(program, 12, 2))
print('Teil 2:', find_combination())
