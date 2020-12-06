with open('./data/day06.txt') as file:
    groups = [set(group.replace('\n', '')) for group in file.read().split('\n\n')]

print('Teil 1:', sum(len(group) for group in groups))


with open('./data/day06.txt') as file:
    groups = [set.intersection(*[set(person) for person in group.split('\n')]) for group in file.read().split('\n\n')]

print('Teil 2:', sum(len(group) for group in groups))
