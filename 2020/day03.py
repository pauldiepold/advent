def processInput(row):
    row = [tree for tree in row.replace('\n', '')]
    row = list(map(lambda tree: tree == '#', row))
    return row


inputFile = open('data/day03.txt', "r")
trees = inputFile.readlines()
trees = list(map(processInput, trees))

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

result = 1

for slope in slopes:
    counter = 0
    for i in range(len(trees))[0::slope[1]]:
        if trees[i][(slope[0] * int(i / slope[1])) % len(trees[0])]:
            counter += 1
    print(counter)
    result = result * counter

print(result)
