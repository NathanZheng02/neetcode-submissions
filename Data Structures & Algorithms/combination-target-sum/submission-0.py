class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, combo, total):
            if total == target:
                res.append(combo.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            combo.append(nums[i])
            dfs(i, combo, total + nums[i])

            combo.pop()
            dfs(i + 1, combo, total)
        dfs(0, [], 0)
        return res