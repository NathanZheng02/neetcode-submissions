class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Time Complexity: O(m * n)
        # Space Compleixty: O(m * n)
        # dp = [[1] * (n) for _ in range(m)]
        # for r in range(1, m):
        #     for c in range(1, n):
        #         dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        # print(dp)
        # return dp[-1][-1]

        # Time Complexity: O(m * n)
        # Space Compleixty: O(n)
        # Utilize the fact that we are going 1 row at a time
        # and that dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        # can be simplified into dp[c] = dp[c] + dp[c - 1]
        # bc we already have the previous row saved.
        dp = [1] * n
        for r in range(1, m):
            for c in range(1, n):
                dp[c] += dp[c - 1]
        return dp[-1]

