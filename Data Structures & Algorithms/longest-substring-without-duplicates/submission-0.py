class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # We can use a sliding window
        window = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            # If the current element exists in the window,
            # remove elements from the left until it is gone
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])

            # Check length
            length = right - left + 1
            if length > max_len:
                max_len = length

        return max_len
