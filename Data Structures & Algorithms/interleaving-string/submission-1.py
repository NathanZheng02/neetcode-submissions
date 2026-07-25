class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        
        # The first row/column is for base case where we
        # want to check to see if parts of s1 or s2
        # are in s3.
        dp = [[False] * (n + 1) for _ in range(m + 1)] # s1 x s2
        
        # Base Case
        dp[0][0] = True

        
        for r in range(m + 1):
            for c in range(n + 1):
                # If it is not the first row, we check if we have previously used
                # from s1 and mark it as true if the chars in s1 and s3 are equal
                if r > 0 and s1[r - 1] == s3[c + r - 1] and dp[r - 1][c]:
                    dp[r][c] = True
                if c > 0 and s2[c - 1] == s3[c + r - 1] and dp[r][c - 1]:
                    dp[r][c] = True
                
        print(dp)
        return dp[-1][-1]