class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = {0:0,1:0,2:0}
        for i in nums:
            a[i]+=1
        for i in range(a[0]):
            nums[i]= 0
        for i in range (a[0],a[0]+a[1]):
            nums[i] = 1
        for i in range(a[0]+a[1],a[0]+a[1]+a[2]):
            nums[i] = 2
