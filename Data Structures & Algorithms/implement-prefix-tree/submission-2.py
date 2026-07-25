class Node:
    def __init__(self):
        self.children = {} # Map: {curr children, next nodes}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            # Create new node
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        # Check if this is end of word vs prefix
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True
        