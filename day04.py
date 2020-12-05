import string


def processInput(line):
    return line.replace('\n', '').split()


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

    hgt = passport['hgt']
    if not ((hgt[-2:] == 'cm' and len(hgt) == 5 and 150 <= int(hgt[0:3]) <= 193) or
            (hgt[-2:] == 'in' and len(hgt) == 4 and 59 <= int(hgt[0:2]) <= 76)):
        print(hgt)
        return False

    return True


def keysPresent(passport):
    fields = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid',)
    return all(key in passport for key in fields)


inputFile = open('data/day4.txt', "r")
rows = inputFile.readlines()
rows = list(map(processInput, rows))

passports = []
currentPassport = []

for row in rows:
    if len(row) != 0:
        currentPassport.extend(row)
    else:
        dic = {}
        for item in currentPassport:
            split = item.rsplit(':')
            dic[split[0]] = split[1]
        passports.append(dic)
        currentPassport = []

counter1 = 0
counter2 = 0

for passport in passports:
    if keysPresent(passport):
        counter1 += 1

    if keysPresent(passport) and isValid(passport):
        counter2 += 1

print('Teil 1: ' + str(counter1))
print('Teil 2: ' + str(counter2))
