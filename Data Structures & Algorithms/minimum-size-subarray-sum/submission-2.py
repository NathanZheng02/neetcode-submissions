class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Variable sliding window

        if len(nums) == 1 and nums[0] < target:
            return 0
        if len(nums) == 1 and nums[0] > target:
            return 1
        if len(nums) == 0 and target != 0:
            return 0
        if len(nums) == 0 and target == 0:
            return 0
        left = 0
        right = 0
        total = nums[0]
        res = float("inf")
        while right < len(nums) - 1:
            while total >= target:
                res = min(res, right - left + 1)
                total -= nums[left]
                left += 1
            right += 1
            total += nums[right]
            
        while total >= target:
            res = min(res, right - left + 1)
            total -= nums[left]
            left += 1
        if res == float("inf"):
            return 0
        return res