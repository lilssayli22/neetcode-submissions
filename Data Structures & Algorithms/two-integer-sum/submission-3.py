class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in nums:
            if i in dict1.keys(): 
             if (dict1[i]==i and 2*i==target):
                sol = [nums.index(i),nums.index(i,nums.index(i)+1)]
                return  sol
            dict1[i] = target - i
        
        
        for i in nums:
            if (dict1[i] in nums) and (dict1[i]!=i):
                sol = [nums.index(i),nums.index(dict1[i])]
                return sol
        return None