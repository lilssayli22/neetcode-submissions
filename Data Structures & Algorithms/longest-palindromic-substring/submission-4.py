class Solution:
    def isPalindrome(self, s: str, i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        memo = {}

        def f(i, j):
            if i >= j:
                return (i, j)

            if (i, j) in memo:
                return memo[(i, j)]

            if self.isPalindrome(s, i, j):
                memo[(i, j)] = (i, j)
                return (i, j)

            x1 = f(i + 1, j)
            x2 = f(i, j - 1)
            res = max(x1, x2, key=lambda t: t[1] - t[0])
            memo[(i, j)] = res
            return res

        start, end = f(0, n - 1)
        return s[start:end + 1]
    