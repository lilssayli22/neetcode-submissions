class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        dic = {}
        i = 0
        j = 1
        best = 0
        curr = 1
        dic[s[0]] = 0
        while j < len(s):
            if s[j] not in dic or dic[s[j]] < i:
                dic[s[j]] = j
                curr += 1
                j += 1
            else:
                best = max(curr, best)   
                i = dic[s[j]] + 1
                dic[s[j]] = j
                curr = j - i + 1
                j += 1
        return max(best, curr)