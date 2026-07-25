class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        visited = set()
        minHeap = [[grid[0][0], 0, 0]] # (max_height, r, c)
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        visited.add((0, 0))
        while minHeap:
            maxH, r, c = heapq.heappop(minHeap)

            if r == n - 1 and c == n - 1:
                return maxH
            
            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if (newR not in range(n) or
                    newC not in range(n) or
                    (newR, newC) in visited):
                    continue

                visited.add((newR, newC))
                heapq.heappush(minHeap, [max(maxH, grid[newR][newC]), newR, newC])
        
            
