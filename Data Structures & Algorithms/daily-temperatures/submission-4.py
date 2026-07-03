class Solution:
    def dailyTemperatures(self, temperatures):
        mono_stack = []
        res = [0 for  i in range( len(temperatures))]
        mono_stack.append((temperatures[0],0))
        for i in range(1,len(temperatures)):
            while mono_stack and temperatures[i] > mono_stack[-1][0]:
                a = mono_stack.pop()
                res[a[1]] = i-a[1]
                
            mono_stack.append((temperatures[i],i))
        return res