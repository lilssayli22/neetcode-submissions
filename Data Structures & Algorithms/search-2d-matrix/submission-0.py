class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def searchRow(row):
            if not row:
                return False
            mid = len(row) // 2
            if row[mid] == target:
                return True
            elif target > row[mid]:
                return searchRow(row[mid+1:])
            else:
                return searchRow(row[:mid])

        if len(matrix) == 1:
            return searchRow(matrix[0])

        mid = len(matrix) // 2
        if target > matrix[mid][0]:
            return self.searchMatrix(matrix[mid:], target)
        elif target == matrix[mid][0]:
            return True
        else:
            return self.searchMatrix(matrix[:mid], target)