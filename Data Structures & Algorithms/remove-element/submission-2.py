class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        swap = len(nums)
        i = 0
        while i < swap:
            if nums[i] == val:
                swap -= 1
                nums[i] = nums[swap]
            else:
                i += 1
        return swap
        

