class Node:
    # Constructor
    def __init__(self):
        self.children = {}
        self.end = False

    # Adding a word string to the Trie Graph
    def add_word(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.end = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Create a Trie Graph to store all of the words
        root = Node()
        for word in words:
            root.add_word(word)

        rows, cols = len(board), len(board[0])
        visited = set()
        res = set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                (r, c) in visited or board[r][c] not in node.children):
                return
            
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]

            # If the character added completes a word
            if node.end:
                res.add(word)
            
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            visited.remove((r, c))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(res)