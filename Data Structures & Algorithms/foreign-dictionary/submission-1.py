class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c : set() for w in words for c in w}

        for i in range(len(words) - 1):
            first, sec = words[i], words[i + 1]
            minLength = min(len(first), len(sec))

            # Edge Case
            if first[:minLength] == sec[:minLength] and len(sec) < len(first):
                return ""
            
            for j in range(minLength):
                # Find first char that doesn't match and add that to list
                if first[j] != sec[j]:
                    adj[first[j]].add(sec[j])
                    break
        
        visited = {} # Map each char with False = visited and True = curr path
        res = []

        def dfs(node):
            if node in visited:
                return visited[node]
            
            visited[node] = True
            for nei in adj[node]:
                if dfs(nei):
                    return True

            visited[node] = False
            res.append(node)

        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)

