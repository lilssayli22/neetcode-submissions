class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)

        def indice_min(g, cible):
            lo, hi = g, n - 1
            res = n
            while lo <= hi:
                m = (lo + hi) // 2
                if nums[m] >= cible:
                    res = m
                    hi = m - 1
                else:
                    lo = m + 1
            return res

        def indice_max(g, cible):
            lo, hi = g, n - 1
            res = g - 1
            while lo <= hi:
                m = (lo + hi) // 2
                if nums[m] <= cible:
                    res = m
                    lo = m + 1
                else:
                    hi = m - 1
            return res

        total = 0
        for i in range(n):
            mn = indice_min(i + 1, lower - nums[i])
            mx = indice_max(i + 1, upper - nums[i])
            if mn <= mx:
                total += mx - mn + 1
        return total