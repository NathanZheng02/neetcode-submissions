class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPali(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            # Check without left and without right
            return checkPali(l + 1, r) or checkPali(l, r - 1)
        
        return True