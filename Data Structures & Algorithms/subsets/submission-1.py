class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # We can either use the current nums index or not use it
        res = []

        combo = []
        def backtrack(i):
            if i >= len(nums):
                res.append(combo.copy())
                return

            # Include nums[i]
            combo.append(nums[i])
            backtrack(i + 1)
            
            # Not include nums[i] (popping nums[i])
            combo.pop()
            backtrack(i + 1)
        
        backtrack(0)
        return res


            