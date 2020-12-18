import numpy as np

with open('./data/day16.txt') as file:
    data = [section.replace('your ticket:\n', '').replace('nearby tickets:\n', '').split('\n')
            for section in file.read().split('\n\n')]

rules = {}
rules_raw = [rule.split(': ') for rule in data[0]]
for name, value in rules_raw:
    ranges = [list(range(int(r.split('-')[0]), int(r.split('-')[1]) + 1)) for r in value.split(' or ')]
    rules[name] = set(ranges[0] + ranges[1])

all_rules = set([k for j in list(rules.values()) for k in j])

tickets = np.array([np.array([int(d) for d in ticket.split(',')]) for ticket in data[2]])

print(rules)

def is_invalid(d):
    return d not in all_rules


print('Teil 1:', sum([d for ticket in tickets for d in ticket if is_invalid(d)]))

valid_tickets = np.array([ticket for ticket in tickets if not any(is_invalid(d) for d in ticket)])
rule_dict = {}
found = True
while len(rules) > 0 and found:
    found = False
    for i in range(len(rules)):
        candidates = [rule for rule, values in rules.items() if all(d in values for d in valid_tickets[:, i])]
        print(valid_tickets[:, i], candidates)
        # print(candidates)
        if len(candidates) == 1:
            found = True
            rule_dict[candidates[0]] = i
            rules.pop(candidates[0])
            # print(i, candidates[0])
print(rule_dict)
