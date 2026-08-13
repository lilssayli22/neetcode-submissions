class Solution:
    def integerBreak(self, n: int) -> int:
        l = {}
        def f(n):
            if n in l:
                return l[n]
            if n == 1:
                return 1
            if n == 2:
                return 1
            a = 1
            for i in range(1, n//2 + 1):
                b = max(i*(n-i), i*f(n-i))
                a = max(a, b)
            l[n] = a
            return l[n]
        return f(n)