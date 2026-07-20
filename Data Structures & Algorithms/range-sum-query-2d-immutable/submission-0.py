from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.rows = len(matrix)
        self.columns = len(matrix[0])
        self.l = []
        for i in range(self.rows):
            for j in range(self.columns):
                self.l.append(matrix[i][j])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = 0
        for i in range(row1, row2 + 1):
            for j in range(col1, col2 + 1):
                total += self.l[i * self.columns + j]
        return total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)