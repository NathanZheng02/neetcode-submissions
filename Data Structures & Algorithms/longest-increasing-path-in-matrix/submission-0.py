class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        memo = {} # Key: (r, c), Val: max length from that spot
        visited = set() # (r, c)

        def backtrack(r, c, prev):
            if (r not in range(rows) or
                c not in range(cols) or matrix[r][c] <= prev):
                return 0
            if (r, c) in memo:
                return memo[(r, c)]

            pathLen = max(backtrack(r + 1, c, matrix[r][c]),
                            backtrack(r - 1, c, matrix[r][c]),
                            backtrack(r, c - 1, matrix[r][c]),
                            backtrack(r, c + 1, matrix[r][c])) + 1
            memo[(r, c)] = pathLen
            return pathLen
            
        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in memo:
                    backtrack(r, c, float("-inf"))
        return max(memo.values())
        