class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # Base Case
        if len(nums) == 0:
            return [[]]
        
        # Call without first element
        perms = self.permute(nums[1:])

        # Go through every possible index to insert
        res = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                res.append(p_copy)
        
        return res
