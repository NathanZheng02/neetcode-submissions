class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Either take 1 step of 2 steps
        dp = [0] * (len(cost) + 1)
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, len(dp)):
            dp[i] = min(dp[i - 1], dp[i - 2])
            if i < len(cost):
                dp[i] += cost[i]
        print("Cost: ", dp)
        return dp[-1]