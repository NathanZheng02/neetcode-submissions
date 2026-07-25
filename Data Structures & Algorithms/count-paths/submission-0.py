class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Time Complexity: O(n^2)
        # Space Compleixty: O(n^2)
        dp = [[1] * (n) for _ in range(m)]
        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        print(dp)
        return dp[-1][-1]

