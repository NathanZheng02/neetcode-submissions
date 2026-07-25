class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chars = {}

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            
            count = tuple(count)
            if count in chars:
                chars[count].append(word)
            else:
                chars[count] = [word]
        
        print(chars)
        res = []
        for key, val in chars.items():
            res.append(val)
        return res