class Solution:
    def minimumTotal(self, triangle) -> int:
        memo = {}

        def solve(i, j):
            # Dernière ligne
            if i == len(triangle) - 1:
                return triangle[i][j]

            # Si déjà calculé
            if (i, j) in memo:
                return memo[(i, j)]

            # Les deux choix possibles
            left = solve(i + 1, j)
            right = solve(i + 1, j + 1)

            # Meilleur choix
            memo[(i, j)] = triangle[i][j] + min(left, right)

            return memo[(i, j)]

        return solve(0, 0)
