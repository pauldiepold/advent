def run(program):
    visited = set()
    i = 0
    acc = 0
    while i not in visited:
        visited.add(i)
        if program[i][0] == 'acc':
            acc += int(program[i][1])
            i += 1
        elif program[i][0] == 'jmp':
            i += int(program[i][1])
        elif program[i][0] == 'nop':
            i += 1

        if i >= len(program):
            return acc, True
    return acc, False


with open('data/day08.txt') as file:
    instructions = [instruction.replace('+', '').split(' ') for instruction in file.read().split('\n')]

print('Teil 1:', run(instructions)[0])

for i in range(len(instructions)):

    copy = [x[:] for x in instructions]
    if copy[i][0] == 'jmp':
        copy[i][0] = 'nop'
    elif copy[i][0] == 'nop':
        copy[i][0] = 'jmp'

    acc, no_loop = run(copy)
    if no_loop:
        print('Teil 2:', acc)
        break
