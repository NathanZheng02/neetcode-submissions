class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob1 represents the previous max of -1 house (don't rob curr)
        # rob2 represents the previous max of -2 house that was previously robbed
        rob1, rob2 = 0, 0
        for n in nums:
            best_rob = max(rob1, rob2 + n)
            rob2 = rob1
            rob1 = best_rob
        return rob1