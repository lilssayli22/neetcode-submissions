class Solution:
    def rob(self, nums):
        n = len(nums)
        memo = {}

        def helper(i):
            remaining = n - i
            if remaining == 1:
                return nums[i]
            elif remaining == 2:
                return max(nums[i], nums[i+1])
            elif remaining == 3:
                return max(nums[i] + nums[i+2], nums[i+1])

            if i in memo:
                return memo[i]

            result = max(nums[i] + helper(i+2), nums[i+1] + helper(i+3))
            memo[i] = result
            return result

        return helper(0)