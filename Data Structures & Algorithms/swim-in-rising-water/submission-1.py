class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        visited = set()
        visited.add((0, 0))
        minHeap = [(grid[0][0], 0, 0)] # (max height, r, c)

        while minHeap:
            height, r, c = heapq.heappop(minHeap)

            # Check ending condition
            if r == n - 1 and c == n - 1:
                return height
            
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (neiR not in range(n) or
                    neiC not in range(n) or
                    (neiR, neiC) in visited):
                    continue

                visited.add((neiR, neiC))
                heapq.heappush(minHeap, (max(height, grid[neiR][neiC]), neiR, neiC))

