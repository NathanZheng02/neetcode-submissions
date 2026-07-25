class Solution:
    def longestPalindrome(self, s: str) -> str:
        resL = 0
        resR = 0
        length = 0

        for i in range(len(s)):
            # Odd length
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > length:
                    resL = l
                    resR = r + 1
                    res = s[l:r+1]
                    length = r - l + 1
                l -= 1
                r += 1

            # Even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > length:
                    resL = l
                    resR = r + 1
                    length = r - l + 1
                l -= 1
                r += 1
                
        return s[resL : resR]