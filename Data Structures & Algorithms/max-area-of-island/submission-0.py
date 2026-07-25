class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def bfs(r, c):
            nonlocal max_area
            curr_area = 1
            queue = deque()
            visited.add((r, c))
            queue.append((r, c))

            while queue:
                row, col = queue.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                
                for dr, dc in directions:
                    new_r, new_c = row + dr, col + dc
                    if (new_r in range(rows) and
                        new_c in range(cols) and
                        (new_r, new_c) not in visited and
                        grid[new_r][new_c] == 1):

                        print("Visited ", new_r, ", ", new_c)
                        
                        curr_area += 1
                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))
            max_area = max(max_area, curr_area)
                        
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    print("Started searching: ", r, ", ", c)
                    bfs(r, c)
        
        return max_area