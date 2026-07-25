class Solution:
    def jump(self, nums: List[int]) -> int:
        left, right = 0, 0
        count = 0

        while right < len(nums) - 1:
            far_idx = nums[left]
            for curr in range(left, right + 1):
                far_idx = max(far_idx, curr + nums[curr])
            left = right + 1
            right = far_idx
            count += 1
        return count