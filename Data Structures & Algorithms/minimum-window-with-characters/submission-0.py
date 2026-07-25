class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Variable sliding window that keeps track of the
        # shortest length and the index of the start

        # Edge Cases:
        if t == "":
            return ""
        
        t_map, window = {}, {}
        
        # Store counts for t_map
        for c in t:
            t_map[c] = 1 + t_map.get(c, 0)

        # We have 0, we need unique chars (t_map)
        have, need = 0, len(t_map)
        res, min_len = [-1, -1], float("inf")
        left = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = 1 + window.get(char, 0)

            # Check if the char has the same freq as required in t_map
            if char in t_map and window[char] == t_map[char]:
                have += 1
            
            # Shrink window left to find left bound
            while have == need:
                length = right - left + 1
                if length < min_len:
                    res = [left, right]
                    min_len = length

                # Remove from window and check
                window[s[left]] -= 1
                if s[left] in t_map and window[s[left]] < t_map[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        if min_len != float("inf"):
            return s[l : r + 1]
        else:
            return ""