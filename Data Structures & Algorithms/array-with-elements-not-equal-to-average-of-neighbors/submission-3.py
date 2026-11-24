class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a = sorted(nums) 
        i=0
        while i!=len(nums)-1 : 
            if i == 0:
                i+=1
            elif a[i] == (a[i-1]+a[i+1])/2:
                x = a[i]
                a[i] = a[i+1]
                a[i+1] = x
                i -=1
            else :
                i+=1
        return a