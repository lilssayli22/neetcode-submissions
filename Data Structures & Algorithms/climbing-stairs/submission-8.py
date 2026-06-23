class Solution:
    def __init__(self):
        self.l = [None] * 45
        self.l[0] = 1
        self.l[1] = 2

    def climbStairs(self, n: int) -> int:
        if self.l[n-1] is not None:
            return self.l[n-1]

        self.l[n-1] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.l[n-1]