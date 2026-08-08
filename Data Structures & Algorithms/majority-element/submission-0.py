class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a = {}
        for i in nums:
            if i in a.keys():
                a[i]+=1
            else : 
                a[i]=1
        for k in a.keys():
            if a[k] >int(len(nums)/2):
                return k
                