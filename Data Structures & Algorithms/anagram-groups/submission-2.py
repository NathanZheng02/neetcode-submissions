class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Key of counts of chars, value of list with words in strs
        hm = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            hm[tuple(count)].append(s)
        
        res = []
        for val in hm.values():
            res.append(val)
        return res
            