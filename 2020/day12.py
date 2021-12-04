with open('data/day12.txt') as file:
    actions = [[row[0], int(row[1:])] for row in file.read().split('\n')]


def move(part, actions, ship, direction):
    get_dir = {'N': 1j, 'E': 1, 'S': -1j, 'W': -1}
    get_rot = {90: -1j, 270: 1j}

    for action, value in actions:
        if action == 'F':
            ship += value * direction
        elif value == 180:
            direction *= -1
        elif action == 'R':
            direction *= get_rot[value]
        elif action == 'L':
            direction *= -1 * get_rot[value]
        else:
            if part - 1:
                direction += get_dir[action] * value
            else:
                ship += get_dir[action] * value
    return int(abs(ship.real) + abs(ship.imag))


print('Teil 1:', move(1, actions, 0 + 0j, 1 + 0j))
print('Teil 2:', move(2, actions, 0 + 0j, 10 + 1j))
