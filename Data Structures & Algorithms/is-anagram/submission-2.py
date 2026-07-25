class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        for c in s:
            countS[c] = 1 + countS.get(c, 0)
        countT = {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        return countS == countT