with open('data/day06.txt') as file:
    groups = file.read().split('\n\n')


distinct_answers = [set(group.replace('\n', '')) for group in groups]

print('Teil 1:', sum(len(group) for group in distinct_answers))


intersected_answers = [set.intersection(*[set(person) for person in group.split('\n')]) for group in groups]

print('Teil 2:', sum(len(group) for group in intersected_answers))
