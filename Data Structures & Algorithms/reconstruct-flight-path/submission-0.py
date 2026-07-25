class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        
        # Adding to the dictionary with sorted(tickets) backwards
        # in order to get a stack-like feature where the last
        # value added is the smallest lexi
        for src, dest in sorted(tickets)[::-1]:
            adj[src].append(dest)
        
        res = []
        def dfs(src):
            while adj[src]:
                # Popping smallest lexi and traverse
                dest = adj[src].pop()
                dfs(dest)
            res.append(src)
        
        dfs("JFK")
        return res[::-1]