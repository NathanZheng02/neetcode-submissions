class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for string in strs:
            count_arr = [0] * 26
            # Count each char
            for char in string:
                count_arr[ord(char) - ord("a")] += 1
            if tuple(count_arr) not in hm:
                hm[tuple(count_arr)] = [string]
            else:
                hm[tuple(count_arr)].append(string)
        return list(hm.values())