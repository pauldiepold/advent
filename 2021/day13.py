import numpy as np
import matplotlib.pyplot as plt


def fold_paper(grid, axis, line):
    line = int(line)
    if axis == 'y':
        new_grid = grid[:, :line] + grid[:, :line:-1]
    else:
        new_grid = grid[:line, :] + grid[:line:-1, :]

    return new_grid


if __name__ == "__main__":
    with open('data/day13.txt') as file:
        dots, folds = file.read().split('\n\n')

    dots = np.array([[int(i) for i in line.split(',')] for line in dots.split('\n')])
    folds = [line.split(' ')[2].split('=') for line in folds.split('\n')]

    xmax, ymax = dots[:, 0].max(), dots[:, 1].max()
    paper = np.zeros((xmax + 1, ymax + 1))

    for dot in dots:
        paper[dot[0], dot[1]] = 1

    for fold in folds:
        paper = fold_paper(paper, *fold)
        print(np.count_nonzero(paper))

    plt.imshow(paper.T > 0)
    plt.show()
