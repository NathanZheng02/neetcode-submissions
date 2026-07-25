class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # The KEY to this question is that if the 2 chars from s
        # and t are equal, you can increment both of them by 1
        # OR only increment s and search for future current t values

        m, n = len(s), len(t)
        if m < n:
            return 0
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base Case: If t is "", then only 1 possible case
        for row in range(m + 1):
            dp[row][0] = 1

        for r in range(1, m + 1):
            for c in range(1, n + 1):
                # If the chars are equal, we can match
                # the char in s to a char in t (dp[r - 1][c - 1]) OR
                # we can not map it

                # We don't have a match OR we don't link up the
                # current t char to the current s char when they are equal
                dp[r][c] = dp[r - 1][c]

                # Now with the s char, we link it to the t char if
                # the chars are equal
                if s[r - 1] == t[c - 1]:
                    dp[r][c] += dp[r - 1][c - 1]
        
        # Debugging:
        # print("DP Table: \n")
        # for r in range(m + 1):
        #     for c in range(n + 1):
        #         print(str(dp[r][c]), end = " ")
        #     print("\n")
        return dp[-1][-1]
        