class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0

        memo = {}

        def solve(start: int) -> int:
            if start >= n:
                return 0
            if start in memo:
                return memo[start]
            buy = prices[start]
            best = 0
            for i in range(start, n):
                profit = prices[i] - buy + solve(i + 1)
                if profit > best:
                    best = profit
            memo[start] = best
            return best

        return solve(0)