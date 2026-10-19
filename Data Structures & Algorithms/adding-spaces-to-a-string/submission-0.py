class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i=-1
        j=0
        res = ""
        while j!=len(spaces) : 
            if i+1 == spaces[j] : 
                res +=" "+s[i+1]
                i+=1
                j+=1
            else :
                res+=s[i+1]
                i+=1
        for k in range (i,len(s)-1):
            res +=s[k+1]
        return res
                
