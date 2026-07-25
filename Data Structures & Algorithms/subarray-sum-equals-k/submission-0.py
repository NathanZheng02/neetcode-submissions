class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # We have to keep track of sums of previous totals
        # and see if we can create a subarray of size k.
        # Curr Total - Prev Prefix Total = k

        curr_sum = 0
        prevTotals = {0 : 1} # Start with 0
        res = 0

        for num in nums:
            curr_sum += num
            diff = curr_sum - k

            res += prevTotals.get(diff, 0)
            prevTotals[curr_sum] = 1 + prevTotals.get(curr_sum, 0)
        
        return res