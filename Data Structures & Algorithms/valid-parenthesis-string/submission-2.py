class Solution:
    def checkValidString(self, s: str) -> bool:
        # Range for wild cards
        openMin = openMax = 0

        for i, c in enumerate(s):
            if c == '(':
                openMin += 1
                openMax += 1
            elif c == ')':
                openMin -= 1
                openMax -= 1
            else:
                openMin -= 1
                openMax += 1

            # If at any point the max possiblities is < 0, that means
            # it is some pattern like this: "))))((****"
            if openMax < 0:
                return False

            if openMin < 0:
                openMin = 0

        return openMin == 0