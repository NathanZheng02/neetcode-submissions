class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base Case: If t is "", then only 1 possible case
        for row in range(m + 1):
            dp[row][0] = 1

        for r in range(1, m + 1):
            for c in range(1, n + 1):
                # Shifting pointer if they don't match
                dp[r][c] = dp[r - 1][c]

                # Otherwise, we reupdate dp[r][c] by shifting both pointers
                if s[r - 1] == t[c - 1]:
                    dp[r][c] += dp[r - 1][c - 1]
        print(dp)
        return dp[-1][-1]
        