class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        combo = []

        def dfs(i):
            # If it got to the end, then it passed all pali checks
            if i >= len(s):
                print("End: ", combo, "\n")
                res.append(combo.copy())
                return

            # Check each partition to see if it is a palidrome
            for j in range(i, len(s)):
                if self.palidrome(s, i, j):
                    combo.append(s[i : j + 1])
                    print("Combo: ", combo)
                    dfs(j + 1)
                    combo.pop()

        dfs(0)
        return res
    
    def palidrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
