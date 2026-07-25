class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        mapS = Counter(s)
        mapT = Counter(t)

        for key, val in mapT.items():
            if key not in mapS or val > mapS[key]:
                return key
        