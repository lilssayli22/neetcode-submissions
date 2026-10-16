class Solution:
    def moveZeroes(self, nums) -> None:
        k = 0  # prochaine position pour un non-zéro
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[k], nums[j] = nums[j], nums[k]
                k += 1