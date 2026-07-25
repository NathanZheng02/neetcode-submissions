class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Map each nums[i] to nums[i] - 1 index
        # Start by removing negatives
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        # Now mark indices with negatives. If 0, mark it with value
        # - len(nums)
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if index in range(len(nums)):
                if nums[index] > 0:
                    nums[index] = -nums[index]
                elif nums[index] == 0:
                    nums[index] = -(len(nums) + 1)

        # Now return first instance of non negative
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i + 1
        return len(nums) + 1
