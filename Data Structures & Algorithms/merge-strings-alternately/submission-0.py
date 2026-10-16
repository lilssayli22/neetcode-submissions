class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        test = False
        j = 0
        final = ""
        while i<len(word1) and j < len(word2):
            if test ==False:
                final+=word1[i]
                i+=1
                test=True
            else : 
                final+=word2[j]
                j+=1
                test=False
        if i==len(word1) : 
            for k in range(j,len(word2)):
                final +=word2[k]
        if j==len(word2) : 
            for k in range(i,len(word1)):
                final +=word1[k]

        return final