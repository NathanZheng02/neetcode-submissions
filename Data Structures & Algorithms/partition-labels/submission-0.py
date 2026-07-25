class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastAppear = {}
        for i, c in enumerate(s):
            lastAppear[c] = i
        
        res = []
        size = end = 0

        for i, c in enumerate(s):
            size += 1
            end = max(end, lastAppear[c])

            if end == i:
                res.append(size)
                size = 0
        
        return res
                
