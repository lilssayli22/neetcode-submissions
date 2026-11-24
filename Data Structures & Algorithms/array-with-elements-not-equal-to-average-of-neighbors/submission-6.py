class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        a = sorted(nums)
        n = len(a)
        if n == 3:
            if 2 * a[1] == a[0] + a[2]:
                a[0], a[1] = a[1], a[0]
            return a
        i = 1
        while i < n - 1:
            if 2 * a[i] == a[i-1] + a[i+1]:
                j = i + 2 if i + 2 < n else 0
                a[i+1], a[j] = a[j], a[i+1]
                i = max(1, i - 1)
            else:
                i += 1
        return a