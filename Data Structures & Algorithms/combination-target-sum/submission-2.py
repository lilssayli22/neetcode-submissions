class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        def backtracking(paths,i,sums):
            if sums == target :
                results.append(paths[:])
                return
            if sums!=target and i>=len(nums) : 
                return
            if (sums + nums[i]) <= target :
                paths.append(nums[i])
                sums+=nums[i]
                backtracking(paths,i,sums)
                paths.pop()
                sums-=nums[i]
            backtracking (paths,i+1,sums)
        backtracking([],0,0)
        return results
