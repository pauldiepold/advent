import numpy as np
import re


class Board:
    def __init__(self, raw_board):
        self.board = self.parse_input(raw_board)
        self.marked = np.zeros((5, 5), dtype=bool)
        self.has_won = False

    def parse_input(self, string):
        return np.array([[int(x) for x in re.sub(' +', ' ', line).strip().split(' ')] for line in string.split('\n')])

    def mark_number(self, number):
        indices = np.argwhere(self.board == number)
        if len(indices) == 1:
            self.marked[indices[0][0], indices[0][1]] = True

    def check_for_win(self):
        for x in range(5):
            if np.all(self.marked[:, x]) or np.all(self.marked[x, :]):
                self.has_won = True

    def get_unmarked_sum(self):
        return np.sum(self.board, where=np.invert(self.marked))


with open('data/day04.txt') as file:
    lines = [line for line in file.read().split('\n\n')]

drawn_numbers = [int(x) for x in lines[0].split(',')]
boards = [Board(b) for b in lines[1:]]

score1 = 0
score2 = 0

for drawn_number in drawn_numbers:
    for board in boards:
        board.mark_number(drawn_number)
        board.check_for_win()

        # Part 1
        if board.has_won and not score1:
            score1 = board.get_unmarked_sum() * drawn_number

        # Part 2
        if all([b.has_won for b in boards]):
            score2 = board.get_unmarked_sum() * drawn_number
            break

    if score1 and score2:
        break

print(f'Part 1: {score1}')
print(f'Part 2: {score2}')
