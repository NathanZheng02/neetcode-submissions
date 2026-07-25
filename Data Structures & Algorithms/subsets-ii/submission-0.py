class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        combo = []
        def dfs(i):
            if i >= len(nums):
                res.append(combo.copy())
                return
            combo.append(nums[i])
            dfs(i + 1)
            combo.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)
        dfs(0)
        return res