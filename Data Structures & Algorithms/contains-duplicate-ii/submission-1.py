class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        i = 0
        j = 1
        while i < len(nums) - 1:
            if nums[i] == nums[j] and j - i <= k:
                return True
            if j - i < k and j + 1 < len(nums):
                j += 1
            else:
                i += 1
                j = i + 1
        return False