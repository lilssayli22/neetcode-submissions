class Solution:
    def combinationSum4(self, nums, target: int) -> int:
        l={}
        def f(target) :
            if target in l.keys():
                return l[target]
            a=0
            for i in nums : 
                if i==target:
                    a+= 1
                else :
                    if target> i:
                        a+= 1*f(target-i)
            l[target] = a
            return a
        f(target)
        return l[target]