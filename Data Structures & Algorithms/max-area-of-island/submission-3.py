class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def dfs(r, c):
            if (r not in range(rows) or
                c not in range(cols) or
                grid[r][c] != 1 or
                (r, c) in visited):

                return 0

            visited.add((r, c))
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) +
                    dfs(r, c + 1) + dfs(r, c - 1))
                        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    max_area = max(dfs(r, c), max_area)
        
        return max_area