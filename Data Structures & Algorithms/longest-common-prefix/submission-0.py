class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        idx = 0
        while idx < len(strs[0]):
            c = strs[0][idx]
            for i in range(1, len(strs)):
                newString = strs[i]
                if idx >= len(newString) or newString[idx] != c:
                    return res
            res = res + c
            idx += 1
        return res