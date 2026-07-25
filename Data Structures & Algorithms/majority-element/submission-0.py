class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, res = 0, nums[0]
        for i in range(len(nums)):
            if res == nums[i]:
                count += 1
            else:
                count -= 1
            
            if count < 0:
                count = 1
                res = nums[i]
        return res