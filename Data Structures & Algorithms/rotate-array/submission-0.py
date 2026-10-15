class Solution:
    def rotate(self, nums, k: int) -> None:
        n = len(nums)
        k %= n
        nombre = 0
        start = 0
        while nombre < n:
            i = start
            a = nums[start]
            while True:
                j = (i + k) % n
                b = nums[j]
                nums[j] = a
                a = b
                i = j
                nombre += 1
                if i == start:      # cycle terminé
                    break
            start += 1              # on passe au cycle suivant