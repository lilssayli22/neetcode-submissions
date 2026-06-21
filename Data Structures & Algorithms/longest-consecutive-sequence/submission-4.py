class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums : 
            return 0
        l=[]
        maxx = nums[0]
        minn = nums[0]
        for i in nums:
            if i<minn : 
                minn = i
            if i >  maxx : 
                maxx = i
        l = [i for i in range(minn , maxx+1)]
        ll = set(nums)
        new_l =[]
        for i in range(len(l)):
            if l[i] in ll:
                new_l.append(l[i])
            else:
                new_l.append('#')
        new_l.append('#')
        res = 0
        final_res = 0
        shabang_found = False
        for i in new_l:
            if i!="#":
                res +=1
            else:
                shabang_found = True
                if (res > final_res):
                    final_res = res
                res = 0
        if shabang_found == False :
            return res
        
        
        return final_res