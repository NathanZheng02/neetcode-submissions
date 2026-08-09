class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Binary search
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2)
            print(mid)

            # Go left if less, go right if larger, else we have found it
            if target < nums[mid]:
                r = mid - 1
            elif target > nums[mid]:
                l = mid + 1
            else:
                return mid

        return l
