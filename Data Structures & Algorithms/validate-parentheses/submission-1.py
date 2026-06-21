from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        d = deque([])
        for i in s:
            if i==')':
                if len(d)==0:
                    return False
                x = d.pop()
                if x !="(":
                    return False
            elif i==']':
                if len(d)==0:
                    return False
                x = d.pop()
                if x !="[":
                    return False
            elif i=='}':
                if len(d)==0:
                    return False
                x = d.pop()
                if x !="{":
                    return False
            else : 
                d.append(i)
        if len(d) != 0:
            return False
        return True