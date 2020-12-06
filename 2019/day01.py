import math

with open('./data/day01.txt') as file:
    modules = file.read().split('\n')

modules_fuel = sum(fuel for fuel in [math.floor(int(module) / 3) - 2 for module in modules])

print('Teil 1:', modules_fuel)


def recursive_fuel(mass):
    fuel = math.floor(int(mass) / 3) - 2
    if fuel <= 0:
        return 0
    else:
        return fuel + recursive_fuel(fuel)


modules_fuel = sum(fuel for fuel in [recursive_fuel(module) for module in modules])

print('Teil 2:', modules_fuel)
