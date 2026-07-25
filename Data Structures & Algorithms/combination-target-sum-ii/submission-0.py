class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, combo, total):
            if total == target:
                res.append(combo.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            combo.append(candidates[i])
            dfs(i + 1, combo, total + candidates[i])
            combo.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, combo, total)
        dfs(0, [], 0)
        return res