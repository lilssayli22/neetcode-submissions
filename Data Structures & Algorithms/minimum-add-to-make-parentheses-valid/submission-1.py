class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        queue = []
        i = 0
        queue.append(s[i])
        i+=1
        while i != len(s) :
            if queue == [] : 
                queue.append(s[i])
                i+=1
            elif queue[-1] == '(' and s[i] ==')' :
                queue.pop()
                i+=1
            else :
                queue.append(s[i])
                i+=1
        return len(queue)