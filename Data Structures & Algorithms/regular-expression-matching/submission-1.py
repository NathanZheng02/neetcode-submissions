class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Both out of bounds means all pattern matches all of s
            if i >= len(s) and j >= len(p):
                return True
            
            # Otherwise, if pattern has no more vals to match, then it is not possible
            if j >= len(p):
                return False
            
            matching = i < len(s) and (s[i] == p[j] or p[j] == ".")
            
            # Handle star
            if (j + 1 < len(p)) and p[j + 1] == "*":
                memo[(i, j)] = (dfs(i, j + 2) or
                                (matching and dfs(i + 1, j)))
                return memo[(i, j)]
            # Check matching
            if matching:
                memo[(i, j)] = dfs(i + 1, j + 1)
                return memo[(i, j)]
            
            # Not matching
            memo[(i, j)] = False
            return False
        
        return dfs(0, 0)

            