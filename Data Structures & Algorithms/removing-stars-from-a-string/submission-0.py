class Solution:
    def removeStars(self, s: str) -> str:
        l=[]
        i = 0
        l.append(s[i])
        i+=1
        while i!=len(s) : 
            if s[i] == "*" : 
                l.pop()
                i+=1
            else : 
                l.append(s[i])
                i+=1
        a = ''
        for i in l:
            a+=i
        return a
