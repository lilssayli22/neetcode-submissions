class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return nums.index(max(nums))
        i = len(nums) // 2
        if nums[i-1] < nums[i] > nums[i+1]:
            return i
        elif nums[i+1] > nums[i]:
            return i + 1 + self.findPeakElement(nums[i+1:])
        else:
            return self.findPeakElement(nums[:i])