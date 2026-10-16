class Solution:
    def validPalindrome(self, s: str) -> bool:
        def f(s,i,n,deleted) : 
            if i>=n:
                return True
            else :
                if s[i] == s[n]:
                    return True and f(s,i+1,n-1,deleted)
                else : 
                    if deleted == True:
                        return False
                    else : 
                        return f(s,i,n-1,True) or f(s,i+1,n,True)
        return f(s,0,len(s)-1,False)