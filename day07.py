def find(color, bags):
    filtered = [k for k, v in rules.items() if any(color in i for i in v)]
    for filtered_color in filtered:
        bags.add(filtered_color)
        bags = find(filtered_color, bags)
    return bags


def count(color, bags, f):
    for bag in rules[color]:
        bags += f * bag[1]
        bags = count(bag[0], bags, f * bag[1])
    return bags


with open('./data/day07.txt') as file:
    lines = [rule for rule in file.read().split('\n')]

rules = {}
for rule in lines:
    color, contains = rule.split(' bags contain ')
    if contains == 'no other bags.':
        contains = []
    else:
        contains = [[color[2:], int(color[0])] for color in
                    contains.replace('.', '').replace(' bags', '').replace(' bag', '').split(', ')]
    rules[color] = contains

print('Teil 1:', len(find('shiny gold', set())))
print('Teil 2:', count('shiny gold', 0, 1))
