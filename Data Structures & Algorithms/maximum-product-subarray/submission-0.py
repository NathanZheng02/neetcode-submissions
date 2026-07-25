class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Keep track of the max value and a min value for negative
        # flipping maximas
        res = nums[0]
        maxi, mini = 1, 1

        for num in nums:
            currVal = maxi * num
            # Max is either (+, -, curr)
            maxi = max(num * maxi, num * mini, num)
            # Min is either (max turned negative, old min * + val, new val)
            mini = min(currVal, num * mini, num)
            res = max(res, maxi)
            
        return res
