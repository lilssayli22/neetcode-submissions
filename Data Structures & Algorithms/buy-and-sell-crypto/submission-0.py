class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) ==1:
            return 0
        i = 0
        j = 1
        
        best = prices[j] - prices[i]
        if best <=0 : 
            best =0
        while i!=len(prices) and j<len(prices):
                a = prices[j] - prices[i]
                if a > best:
                    best =a
                if a<=0:
                    i=j
                j=j+1
                    
        return best