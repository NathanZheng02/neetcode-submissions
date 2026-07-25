class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 0 1 Knapsack

        total = 0
        for num in nums:
            total += num
        
        if total % 2 != 0:
            return False
        
        dp = [False] * (total // 2 + 1)
        dp[0] = True
        for num in nums:
            for j in range(total // 2, num - 1, -1):
                # Either use the num or not use it (Group 0 or Group 1)
                dp[j] = dp[j] or dp[j - num]
        return dp[-1]