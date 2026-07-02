class Solution:
    h = {i for i in range(10)} 
    j ={}
    def numDecodings(self, s: str) -> int:
        if (s in self.j.keys()):
            return self.j[s]
        if s[0]=='0':
            self.j[s] = 0
            return 0
        if int(s) in self.h:
            self.j[s] = 1
            return 1

        else:
            x = s[:2]
            y=s[:1]
            a=0
            b=0
            if 0<int(x)<=26:
                if (len(s[2:])==0):
                    a =  1
                else:
                 a= self.numDecodings(s[2:])
            if 0<int(y)<=26:
                b = self.numDecodings(s[1:])
            self.j[s] = a+b
            return self.j[s]