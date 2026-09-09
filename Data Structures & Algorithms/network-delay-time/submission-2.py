class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Adjacency List
        edges = defaultdict(list)
        for u, v, time in times:
            edges[u].append((v, time))
        
        # Add starting
        minHeap = [(0, k)] # (Time, Node)
        visited = set()
        minTime = 0

        while minHeap:
            time, node = heapq.heappop(minHeap)

            if node in visited:
                continue
            
            visited.add(node)
            minTime = time

            for nei, wei in edges[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (time + wei, nei))

        # Return minTime it takes to reach all nodes, otherwise -1
        return minTime if len(visited) == n else -1