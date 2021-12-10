def navigation(data):
    match = {'(': ')', '[': ']', '{': '}', '<': '>'}
    points1 = {')': 3, ']': 57, '}': 1197, '>': 25137}
    points2 = {'(': 1, '[': 2, '{': 3, '<': 4}
    result1 = 0
    scores = []

    for line in data:
        stack = []
        corrupted = False
        for c in line:
            if c in match:
                stack.append(c)
            else:
                if c != match[stack.pop()]:
                    result1 += points1[c]
                    corrupted = True

        if not corrupted:
            score = 0
            for c in stack[::-1]:
                score *= 5
                score += points2[c]
            scores.append(score)

    result2 = sorted(scores)[int(len(scores) / 2)]

    return result1, result2


if __name__ == "__main__":
    with open('data/day10.txt') as file:
        lines = [[c for c in line] for line in file.read().split('\n')]

    print(navigation(lines))
