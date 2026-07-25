class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        time = 0
        fresh_oranges = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append([r, c])
                if grid[r][c] == 1:
                    fresh_oranges += 1

        while queue and fresh_oranges > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    new_r, new_c = dr + r, dc + c
                    if (new_r not in range(rows) or
                        new_c not in range(cols) or
                        grid[new_r][new_c] != 1):
                        continue

                    grid[new_r][new_c] = 2
                    queue.append([new_r, new_c])
                    fresh_oranges -= 1
            time += 1
        
        return time if fresh_oranges == 0 else -1

