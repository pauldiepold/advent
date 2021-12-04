import string
import re


def keysPresent(passport):
    return all(key in passport for key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])


def isValid(passport):
    if not (1920 <= int(passport['byr']) <= 2002):
        return False

    if not (2010 <= int(passport['iyr']) <= 2020):
        return False

    if not (2020 <= int(passport['eyr']) <= 2030):
        return False

    if not (passport['hcl'][0] == '#' and len(passport['hcl']) == 7 and
            all(c in string.hexdigits for c in passport['hcl'][-6:])):
        return False

    if not (passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
        return False

    if not (len(passport['pid']) == 9 and all(c in string.digits for c in passport['pid'])):
        return False

    if not ((passport['hgt'][-2:] == 'cm' and len(passport['hgt']) == 5 and 150 <= int(passport['hgt'][0:3]) <= 193) or
            (passport['hgt'][-2:] == 'in' and len(passport['hgt']) == 4 and 59 <= int(passport['hgt'][0:2]) <= 76)):
        return False

    return True


with open('data/day04.txt') as file:
    passports = [dict(x.split(':') for x in re.split(' |\n', line)) for line in file.read().split('\n\n')]

counter1 = 0
counter2 = 0

for passport in passports:
    if keysPresent(passport):
        counter1 += 1

    if keysPresent(passport) and isValid(passport):
        counter2 += 1

print('Teil 1: ' + str(counter1))
print('Teil 2: ' + str(counter2))
