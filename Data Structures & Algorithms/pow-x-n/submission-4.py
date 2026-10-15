class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n>0: 
            if n==1 : 
                return x
            else : 
                if n%2 == 0:
                    return self.myPow(x*x,n/2)
                else : 
                    return x*self.myPow(x*x,(n-1)/2)
        elif n<0 : 
            return 1/self.myPow(x,-n)
        else :
            return 1