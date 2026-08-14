from functools import lru_cache

class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        return max(self._rob_line(nums[:-1]), self._rob_line(nums[1:]))

    def _rob_line(self, arr):
        arr = tuple(arr)

        @lru_cache(maxsize=None)
        def dp(i):
            if i < 0:
                return 0
            return max(dp(i - 1), arr[i] + dp(i - 2))

        return dp(len(arr) - 1)