class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {} # (idx, ways)

        def dfs(i, currSum):
            if i == len(nums):
                return 1 if currSum == target else 0
            if i in memo:
                return memo[i]
            
            return (dfs(i + 1, currSum + nums[i]) +
                    dfs(i + 1, currSum - nums[i]))


        return dfs(0, 0)