class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # Adjacency list where we map the missing char pattern to a list of words
        # that fits the criteria
        adj = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                adj[pattern].append(word)
        
        visited = set([beginWord])
        queue = deque([beginWord])
        length = 1

        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return length
                
                # Get neighbors based on adj
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neiWord in adj[pattern]:
                        if neiWord not in visited:
                            visited.add(neiWord)
                            queue.append(neiWord)

            length += 1
    
        return 0

        
