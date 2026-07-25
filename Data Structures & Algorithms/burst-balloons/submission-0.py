class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Chain matrix diagonal dp problem
        n = len(nums)
        new_nums = [1] + nums + [1]

        dp = [[0] * len(new_nums) for _ in range(len(new_nums))]

        # We are looking at each element between the i to j + 1 interval
        # where we select k as the last element to be popped
        for i in range(n, 0, -1):
            for j in range(i, n + 1):
                for k in range(i, j + 1):
                    # Calculate current score if the curr k idx is popped last
                    # We assume everything from i to k - 1 and k + 1 to j
                    # is the subproblem and has been stored in the dp array
                    popLastScore = new_nums[i - 1] * new_nums[k] * new_nums[j + 1]

                    # Add other scores saved in dp
                    popLastScore += dp[i][k - 1] + dp[k + 1][j]

                    dp[i][j] = max(dp[i][j], popLastScore)
        
        # Debugging
        # for r in range(len(dp)):
        #     for c in range(len(dp[0])):
        #         print(dp[r][c], end = " ")
        #     print("\n")
        return dp[1][n]
