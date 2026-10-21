class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        l = []
        i = 0
        l.append((s[0], 1))
        i += 1
        while i != len(s):
            if not l or s[i] != l[-1][0]:
                l.append((s[i], 1))
                i += 1
            else:
                if l[-1][1] + 1 == k:
                    for _ in range(k - 1):
                        l.pop()
                else:
                    l.append((s[i], l[-1][1] + 1))
                i += 1
        return "".join(c for c, _ in l)