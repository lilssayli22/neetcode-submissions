from typing import List

class Solution:
    def valid_line(self, board, n):
        a = set()
        for i in range(len(board)):
            if board[n][i] != '.':
                if board[n][i] in a:
                    return False
                else:
                    a.add(board[n][i])
        return True

    def valid_column(self, board, n):
        a = set()
        for i in range(len(board)):
            if board[i][n] != '.':
                if board[i][n] in a:
                    return False
                else:
                    a.add(board[i][n])
        return True

    def valid_block(self, board, row, col):
        # row, col = top-left corner of the 3×3 block (0, 3, or 6)
        a = set()
        for i in range(3):
            for j in range(3):
                val = board[row + i][col + j]
                if val != '.':
                    if val in a:
                        return False
                    else:
                        a.add(val)
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check all 9 rows
        for n in range(9):
            if not self.valid_line(board, n):
                return False

        # Check all 9 columns
        for n in range(9):
            if not self.valid_column(board, n):
                return False

        # Check all 9 blocks (top-left corners are at 0, 3, 6)
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                if not self.valid_block(board, row, col):
                    return False

        return True