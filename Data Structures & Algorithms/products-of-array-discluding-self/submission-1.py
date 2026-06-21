class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=1
        b=1
        num_zero = 0
        for i in nums:
            if (i!=0):
             a*=i
             b*=i
            else:
                num_zero +=1
                b*=i
            
        if num_zero >=2 :
            return[0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if (nums[i]==0):
                nums[i] = a
            else: 
                nums[i] = b//nums[i]
        return nums