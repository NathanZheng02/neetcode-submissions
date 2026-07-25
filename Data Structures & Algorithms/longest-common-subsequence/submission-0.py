class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # 2D dp
        m, n = len(text1), len(text2)
        dp = [[0] * n for _ in range(m)]
        
        # Base Cases
        print("M: ", m, " and N: ", n)
        # Go through each column
        for fir in range(m):
            if text2[0] == text1[fir]:
                dp[fir][0] = 1
            else:
                dp[fir][0] = dp[fir - 1][0] if fir != 0 else 0
        for sec in range(n):
            if text1[0] == text2[sec]:
                dp[0][sec] = 1
            else:
                dp[0][sec] = dp[0][sec - 1] if sec != 0 else 0

        # DP
        for r in range(1, m):
            for c in range(1, n):
                if text1[r] == text2[c]:
                    dp[r][c] = dp[r - 1][c - 1] + 1
                else:
                    dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])
        print(dp)
        return dp[-1][-1]