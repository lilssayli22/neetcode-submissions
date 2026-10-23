from collections import deque

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def estTerre(i, j):
            return 0 <= i < rows and 0 <= j < cols and grid[i][j] == 1

        def traiter(i, j):
            # nombre de côtés de la case qui touchent l'eau ou le bord
            p = 0
            for di, dj in directions:
                if not estTerre(i + di, j + dj):
                    p += 1
            return p

        def neighbours(i, j):
            # voisins qui sont de la terre
            res = []
            for di, dj in directions:
                if estTerre(i + di, j + dj):
                    res.append((i + di, j + dj))
            return res

        # trouver la première case de terre
        a = None
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    a = (i, j)
                    break
            if a:
                break

        visited = {a}
        aTraiter = deque([a])
        perim = 0

        while aTraiter:
            i, j = aTraiter.popleft()
            perim += traiter(i, j)
            for v in neighbours(i, j):
                if v not in visited:
                    visited.add(v)
                    aTraiter.append(v)

        return perim