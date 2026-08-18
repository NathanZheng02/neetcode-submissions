class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Mapping val and index of value
        hm = {}

        for i, num in enumerate(nums):
            if target - num in hm:
                return [hm[target - num], i]
            else:
                hm[num] = i
        
