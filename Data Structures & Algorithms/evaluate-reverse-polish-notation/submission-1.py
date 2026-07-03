class Solution:
    def evalRPN(self, tokens) -> int:
        # we use a stack so this algo is quit good with O(n) complexity we just need to itere on tokens
        # for spacial complexity we just use to variable so O(1) cause L is limited always to 2 or 1 element ( a constant number)
        l=[]
        a = {"/","-","*","+"}
        for i in tokens : 
            if i not in a:
                l.append(i)
            else: 
                x = l.pop()
                y = l.pop()
                if i == "+":
                    l.append(int(x)+int(y))
                elif i == "*":
                    l.append(int(x)*int(y))
                elif i == "/":
                    l.append(int(y)/int(x))
                else:
                    l.append(int(y)-int(x))
        return int(l[0])