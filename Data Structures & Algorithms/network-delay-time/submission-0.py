class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra's
        edges = collections.defaultdict(list)

        for u, v, weight in times:
            edges[u].append((v, weight))
        
        minHeap = [(0, k)]
        visited = set()
        t = 0

        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            t = weight

            for nei, wei in edges[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (wei + weight, nei))
            
        return t if len(visited) == n else -1
