class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1= {}
        for i in nums:
            if i in dict1.keys():
                dict1[i]+=1
            else:
                dict1[i]=1
        
        l=[]
        for j in range(k):
            maxi = nums[-1]
            for i in dict1.keys():
                if(dict1[i]>dict1[maxi] and i not in l):
                    maxi = i
            while(maxi in nums):
                nums.remove(maxi)
            l.append(maxi)
        return l