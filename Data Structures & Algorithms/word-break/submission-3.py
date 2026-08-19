class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        wordSet = set(wordDict)  # lookup O(1) au lieu de O(n) dans une liste
        memo = {}

        def helper(s):
            if s == "":
                return True
            if s in memo:
                return memo[s]

            x = False
            for i in range(1, len(s) + 1):
                a = s[:i]
                if a in wordSet:
                    if helper(s[i:]):
                        x = True
                        break

            memo[s] = x
            return x

        return helper(s)