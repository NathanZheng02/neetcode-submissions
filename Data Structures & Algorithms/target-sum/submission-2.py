class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for _ in range(len(nums) + 1)] # dp[index][sum] = count
        dp[0][0] = 1

        for i in range(1, len(nums) + 1):
            for curSum, count in dp[i - 1].items():
                # Adding
                newSum = curSum + nums[i - 1]
                dp[i][newSum] += count

                # Subtracting
                newSum = curSum - nums[i - 1]
                dp[i][newSum] += count
        return dp[-1][target]
