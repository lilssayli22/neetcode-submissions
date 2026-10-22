class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtracking (paths,i):
            if i>=len(nums) : 
                results.append(paths[:])
                return
            else : 
                paths.append(nums[i])
                i+=1
                backtracking(paths,i)
                paths.pop()
                backtracking(paths,i)
        backtracking([],0)
        return results
