class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # m, n = len(word1), len(word2)
        # dp = {} # Key = (idx1, idx2), Val = Changes made so far

        # def dfs(i, j):
        #     if i == m:
        #         return n - j
        #     if j == n:
        #         return m - i
        #     if (i, j) in dp:
        #         return dp[(i, j)]
            
        #     if word1[i] == word2[j]:
        #         dp[(i, j)] = dfs(i + 1, j + 1)
        #     else:
        #         dp[(i, j)] = min(dfs(i + 1, j + 1),
        #                             dfs(i, j + 1),
        #                             dfs(i + 1, j)) + 1
        #     return dp[(i, j)]
        
        # return dfs(0, 0)

        m, n = len(word1), len(word2)
        dp = [[float("inf")] * (n + 1) for _ in range(m + 1)]

        for r in range(m + 1):
            dp[r][0] = r
        for c in range(n + 1):
            dp[0][c] = c

        for r in range(1, m + 1):
            for c in range(1, n + 1):
                if word1[r - 1] == word2[c - 1]:
                    dp[r][c] = dp[r - 1][c - 1]
                else:
                    dp[r][c] = min(dp[r][c - 1],
                                    dp[r - 1][c],
                                    dp[r - 1][c - 1]) + 1
        # print(dp)
        return dp[-1][-1]
                

