def processInput(row):
    row = [tree for tree in row.replace('\n', '')]
    row = list(map(lambda tree: tree == '#', row))
    return row


inputFile = open('data/day3.txt', "r")
trees = inputFile.readlines()
trees = list(map(processInput, trees))

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

result = 1
height = len(trees)
width = len(trees[0])

for slope in slopes:
    counter = 0
    for i in range(height):
        if i % slope[1] == 0:
            if trees[i][(slope[0] * i) % width]:
                counter += 1
    result = result * counter

print(result)
