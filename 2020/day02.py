inputFile = open('data/day02.txt', "r")


def seperateLines(line):
    line = line.split()
    line[0] = [int(x) for x in line[0].rsplit("-")]
    line[1] = line[1].replace(":", "")
    return line


passwords = inputFile.readlines()
passwords = list(map(seperateLines, passwords))

counter1 = 0
counter2 = 0
for password in passwords:
    occurrences = password[2].count(password[1])
    if password[0][0] <= occurrences <= password[0][1]:
        counter1 += 1
    if (password[2][password[0][0]-1] != password[1]) ^ (password[2][password[0][1]-1] != password[1]):
        counter2 += 1

print('Teil 1: ' + str(counter1))
print('Teil 2: ' + str(counter2))
