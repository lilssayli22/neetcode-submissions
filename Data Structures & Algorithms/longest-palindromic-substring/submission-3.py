class Solution:
    def isPalindrome(self, s: str, i: int, j: int) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def f(self, s: str, i: int, j: int, memo: dict):
        if i >= j:
            return (i, j)

        if (i, j) in memo:
            return memo[(i, j)]

        if self.isPalindrome(s, i, j):
            memo[(i, j)] = (i, j)
            return (i, j)

        x1 = self.f(s, i + 1, j, memo)
        x2 = self.f(s, i, j - 1, memo)
        res = max(x1, x2, key=lambda t: t[1] - t[0])
        memo[(i, j)] = res
        return res

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        memo = {}
        start, end = self.f(s, 0, n - 1, memo)
        return s[start:end + 1]