class Solution:
    def isPalindrome(self, s: str) -> bool:
        l= []
        for i in s:
            if (65<=ord(i)<=122 or 48<=ord(i)<=56):
                l.append(i.lower())
        for i in range (len(l)//2):
            if(l[i]!=l[-1-i]):
                return False
        return True