class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Variable sliding window:
        # Expand as long as you have a max of k other elements than the majority
        res = 0
        left = 0
        count = {} # O(26)

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            
            # While the length of the window - most frequent > k,
            # that means the window is not valid and we need to 
            # shift the left until it is valid
            while (right - left + 1) - max(count.values()) > k:
                count[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)
        return res