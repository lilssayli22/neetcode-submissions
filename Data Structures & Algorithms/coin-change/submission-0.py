class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def f(rest):
            if rest == 0:
                return 0
            if rest < 0:
                return -1
            if rest in memo:
                return memo[rest]
            best = float("inf")
            for c in coins:
                y = f(rest - c)
                if y != -1:
                    best = min(best, y + 1)
            memo[rest] = -1 if best == float("inf") else best
            return memo[rest]
        return f(amount)