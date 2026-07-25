class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra's: Adjacency List
        edges = defaultdict(list)
        for u, v, time in times:
            edges[u].append((v, time))
        
        minHeap = [(0, k)] # (Time, Node)
        visited = set()
        minTime = 0

        while minHeap:
            time, node = heapq.heappop(minHeap)

            # Check if the node has not already been visited
            if node in visited:
                continue
            
            # Add to visited and update the time
            visited.add(node)
            minTime = time

            # Add neighbors
            for nei, wei in edges[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (time + wei, nei))
        
        # Return if all nodes have been visited
        return minTime if len(visited) == n else -1


