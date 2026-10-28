from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        atraiter = deque()
        number = 0
        pos = 0   # prochaine case à examiner (numérotée de 0 à rows*cols - 1)

        def chercher_first_node():
            nonlocal pos
            while pos < rows * cols:
                i, j = divmod(pos, cols)   # pos -> (ligne, colonne)
                pos += 1
                if grid[i][j] == 1 and (i, j) not in visited:
                    return (i, j)
            return None

        first_node = chercher_first_node()
        while first_node is not None:
            visited.add(first_node)
            atraiter.append(first_node)

            curr = 0
            while atraiter:
                i, j = atraiter.popleft()
                curr +=1
                for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                    ni, nj = i + di, j + dj
                    if (0 <= ni < rows and 0 <= nj < cols
                            and grid[ni][nj] == 1
                            and (ni, nj) not in visited):
                        visited.add((ni, nj))
                        atraiter.append((ni, nj))

            if curr > number :
                number = curr
            first_node = chercher_first_node()

        return number