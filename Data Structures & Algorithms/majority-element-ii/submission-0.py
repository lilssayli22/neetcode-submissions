class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        a={        }
        for i in nums :
            if i in a.keys():
                a[i]+=1
            else:
                a[i]=1
        l=[]
        for j in a.keys():
            if a[j] > len(nums)/3:
                l.append(j)
        return l