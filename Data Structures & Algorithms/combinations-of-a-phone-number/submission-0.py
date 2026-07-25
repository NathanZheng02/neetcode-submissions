class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        translate = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def backtrack(i, combo):
            if len(combo) == len(digits):
                res.append(combo)
                return
            for c in translate[digits[i]]:
                backtrack(i + 1, combo + c)

        if digits:
            backtrack(0, "")

        return res
