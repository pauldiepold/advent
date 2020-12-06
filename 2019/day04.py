counter1 = 0
counter2 = 0

for i in range(136818, 685979 + 1):
    i = [int(d) for d in str(i)]

    adjacent1 = False
    increasing = True
    for j in range(5):
        if i[j] == i[j + 1]:
            adjacent1 = True
        if i[j] > i[j + 1]:
            increasing = False

    j = 0
    adjacent2 = False
    while j < 5 and (not adjacent2):
        if i[j] == i[j + 1] and ((j < 4 and i[j + 1] != i[j + 2]) or j == 4):
            adjacent2 = True
        j_new = j + 1
        while j_new < 5 and i[j] == i[j_new]:
            j_new += 1
        j = j_new

    if adjacent1 and increasing:
        counter1 += 1
    if adjacent2 and increasing:
        counter2 += 1

print('Teil 1:', counter1)
print('Teil 2:', counter2)
