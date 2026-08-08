class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x = ""
        for i in range (len(strs[0])):
            for j in strs:
                if j=="":
                    return x
                if i>=len(j) :
                    return x
                else :
                    if j[i]!=strs[0][i]:
                        return x
            x = x+strs[0][i]
        return x