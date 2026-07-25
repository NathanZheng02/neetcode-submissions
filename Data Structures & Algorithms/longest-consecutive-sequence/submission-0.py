class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # We can create a hashmap and add all of the numbers into it
        # Then we have a running count of the length and check if n - 1 is in the map
        # Find the starting point, and then check if nums + length is in the set.
        hashset = set(nums)
        max_len = 0
        for num in nums:
            length = 1
            if num - 1 not in hashset:
                while num + length in hashset:
                    length += 1
                max_len = max(length, max_len)
        return max_len