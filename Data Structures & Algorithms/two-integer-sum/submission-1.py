class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for i, num in enumerate(nums):
            comp = target - num

            if comp in complement:
                return [complement[comp], i]

            complement[num] = i
        
