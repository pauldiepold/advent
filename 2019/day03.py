def calc_coords(wire, with_steps=False):
    if not with_steps:
        current = [0, 0]
    else:
        current = [0, 0, 0]
    coords = set()
    for direction in wire:
        if direction[0] == 'R':
            x_or_y = 0
            plus_or_minus = 1
        elif direction[0] == 'U':
            x_or_y = 1
            plus_or_minus = 1
        elif direction[0] == 'L':
            x_or_y = 0
            plus_or_minus = -1
        elif direction[0] == 'D':
            x_or_y = 1
            plus_or_minus = -1
        else:
            x_or_y = False
            plus_or_minus = False

        for distance in range(direction[1]):
            current[x_or_y] += plus_or_minus
            if with_steps:
                current[2] += 1
            coords.add(tuple(current))

    return coords


def calc_distance(coord):
    return abs(coord[0]) + abs(coord[1])


with open('./data/day03.txt') as file:
    wires = [[[direction[0], int(direction[1:])] for direction in wire.split(',')] for wire in file.read().split('\n')]

wire_coords = [calc_coords(wire) for wire in wires]
intersections = set.intersection(*wire_coords)
distances = [calc_distance(intersection) for intersection in intersections]

print('Teil 1:', min(distances))


distances_to_intersections = []
wire_coords_with_steps = [calc_coords(wire, True) for wire in wires]
for intersection in intersections:
    distances = [
        [item[2] for item in wire_coord_with_steps if item[0] == intersection[0] and item[1] == intersection[1]]
        for wire_coord_with_steps in wire_coords_with_steps]
    print(distances)
    distances_to_intersections.append(distances[0][0] + distances[1][0])

print('Teil 2:', min(distances_to_intersections))
