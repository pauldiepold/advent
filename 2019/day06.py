with open('./data/day06.txt') as file:
    objects = {orbit[-3:]: orbit[:3] for orbit in file.read().split('\n')}

orbits = 0
for child, parent in objects.items():
    orbits += 1
    while parent in objects:
        orbits += 1
        parent = objects[parent]

print('Teil 1:', orbits)


def find_path(child):
    output = {}
    parent = objects[child]
    count = 0
    while parent != 'COM':
        count += 1
        parent = objects[parent]
        output[parent] = count
    return output


my_path = find_path('YOU')
santas_path = find_path('SAN')

for object, distance in my_path.items():
    if object in santas_path:
        print('Teil 2:', distance + santas_path[object])
        break
