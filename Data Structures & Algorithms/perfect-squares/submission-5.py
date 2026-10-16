import numpy as np

class Solution:
    def numSquares(self, n: int) -> int:
        l={}
        l[1] = 1
        l[3] =3
        l[2] = 2
        def f(origin,n,depth) : 
            if depth > l[origin] :
                return float("inf")
            
            if n in l.keys() and l[n] != float("inf"):
                return l[n]
            if (int(n**(1/2)))**2 == n :
                l[n] = 1
            else : 
                l[n] = float("inf")
                for i in range(int(np.sqrt(n)), 0, -1):
                    depth+=1
                    b = 1+f(n,(n-(i)**2),depth)
                    if b< l[n]:
                        l[n] = b
                    depth -=1
            return l[n]
        l[n] = float("inf")
        f(n,n,0)
        print(l)
        return l[n]