class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c : set() for w in words for c in w}

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            minLen = min(len(word1), len(word2))

            # Case: Prefix same and 2nd word is shorter [Not possible]
            if word1[:minLen] == word2[:minLen] and len(word2) < len(word1):
                return ""
            
            for j in range(minLen):
                if word1[j] != word2[j]:
                    adj[word1[j]].add(word2[j])
                    break
        
        visited = {} # (Char, visited)
        res = []

        # If c is seen in the same dfs loop (cycle), then
        # it is not valid. Else, we are just connecting
        # 2 segmented graphs and it is ok.
        def dfs(c):
            if c in visited:
                return visited[c]
            visited[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visited[c] = False
            res.append(c)

        for c in adj:
            if dfs(c):
                return ""

        res.reverse()
        return "".join(res)