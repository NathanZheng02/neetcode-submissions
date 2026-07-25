class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Union Find
        n = len(edges) + 1

        parent = [i for i in range(n)]

        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return False
            
            parent[p2] = p1
            return True
        
        for n1, n2 in edges:
            # Union Find fails to connect 2 components, that means we are done.
            # Since the graph previously was cycle free with n - 1 edges, adding an edge
            # would complete any cycle, which can be determined if union find fails.
            if union(n1, n2) == False:
                return [n1, n2]
