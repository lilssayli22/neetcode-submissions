class Solution:
    def findMin(self, nums) -> int:
        
       if len(nums) ==1:
           return nums[0]
       elif len(nums) ==2:
           if nums[0]>nums[1]:
               return nums[1]
           else:
               return nums[0]
       a=nums[len(nums)//2]
       if a>nums[-1]:
           return self.findMin(nums[len(nums)//2:])
       else:
           return self.findMin(nums[:(len(nums)//2)+1])