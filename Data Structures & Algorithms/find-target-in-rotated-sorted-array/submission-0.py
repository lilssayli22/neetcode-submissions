class Solution:
    def search(self, nums, target: int) -> int:
        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        if len(nums) == 2:
            if nums[0] == target:
                return 0
            if nums[1] == target:
                return 1
            return -1

        mid = len(nums) // 2
        a = nums[mid]

        if a == target:
            return mid

        if a > nums[-1]:
            # partie gauche [0..mid] triée
            if nums[0] <= target < a:
                return self.search(nums[:mid+1], target)
            else:
                res = self.search(nums[mid:], target)
                if res == -1:
                    return -1
                return mid + res
        else:
            # partie droite [mid..-1] triée
            if a < target <= nums[-1]:
                res = self.search(nums[mid:], target)
                if res == -1:
                    return -1
                return mid + res
            else:
                return self.search(nums[:mid+1], target)