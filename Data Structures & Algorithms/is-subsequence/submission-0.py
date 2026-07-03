class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a = len(s)
        b = len(t)
        i = 0
        j = a-1
        k = 0
        l = b-1
        while i<=j and k<=l:
            if s[i] == t[k]:
                i+=1
            if s[j] == t[l]:
                j-=1
            k+=1
            l-=1
        if j<i : 
            return True
        return False