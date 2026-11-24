class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        a = sorted (people)
        i = 0
        j = len(a) - 1
        total = 0
        while i<=j:
            if a[i]+a[j]<=limit :
                i+=1
                j-=1
                total +=1
            else :
                j-=1
                total+=1
        return total



