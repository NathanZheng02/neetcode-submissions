class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums) * 2):
            idx = i % len(nums)
            res.append(nums[idx])
        return res