class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill) %2 != 0:
            return -1
        else :
            totale =0
            a = sorted(skill)
            i = 0
            j = len(a)-1
            somme = sum(a)
            lenght = len(a)
            while i<j:
                if a[i]+a[j] == somme*2/lenght:
                    totale+= a[i]*a[j]
                    i+=1
                    j-=1
                else : 
                    return -1
            return totale
