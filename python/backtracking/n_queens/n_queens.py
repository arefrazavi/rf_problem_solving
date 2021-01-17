from pprint import pprint
from typing import List

class Solution:
    def __init__(self):
        self.n = 0
        self.solutions = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        chessboard = [['.' for j in range(self.n)] for i in range(self.n)]
        self.find_solution(chessboard)

        return self.solutions

    def find_solution(self, chessboard: list, row_index: int = 0):
        # if row_index == n, it means that we found a solution by placing all the queens in a safe position
        if row_index == self.n:
            solution = [''.join(row) for row in chessboard]
            self.solutions.append(solution)

            return True

        # Only iterate over columns because in each row, exactly one queen is allowed.
        for col_index in range(self.n):
            # Try to find a solution assuming the selected [row_index][col_index] position for the row_index queen.
            if self.is_pos_safe(row_index, col_index, chessboard):
                chessboard[row_index][col_index] = 'Q'
                self.find_solution(chessboard, row_index + 1)
            # Reset the selected position for the row_index queen to explore other positions in the next iteration.
            chessboard[row_index][col_index] = '.'

        return False

    def is_pos_safe(self, row_index: int, col_index: int, chessboard: list):
        # Is there any queen in the same column in previous rows.
        for r in range(row_index):
            if chessboard[r][col_index] == 'Q':
                return False

        # Is there any queen on the same \ diagonal in previous rows.
        r = row_index - 1
        c = col_index - 1
        while r >= 0 and c >= 0:
            if chessboard[r][c] == 'Q':
                return False
            r -= 1
            c -= 1

        # Is there any queen on the same / diagonal in previous rows.
        r = row_index - 1
        c = col_index + 1
        while r >= 0 and c < self.n:
            if chessboard[r][c] == 'Q':
                return False
            r -= 1
            c += 1

        return True

