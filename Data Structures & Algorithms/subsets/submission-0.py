class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # We can either use or not use a num
        res = []

        subset = []
        def dfs(idx):
            if idx >= len(nums):
                res.append(subset.copy())
                return
            
            # Use nums[i]
            subset.append(nums[idx])
            dfs(idx + 1)

            # Not use nums[i]
            subset.pop()
            dfs(idx + 1)
        dfs(0)
        return res
            