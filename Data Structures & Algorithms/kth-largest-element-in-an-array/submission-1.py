class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Quick Sorting with restrictions
        # Average O(n), worst O(n^2)
        k = len(nums) - k

        def quick_search(l, r):
            # Select last element as the pivot
            pivot, p = nums[r], l

            # Range from left to right
            for i in range(l, r):
                # Swap elements smaller than pivot in the range
                if nums[i] <= pivot:
                    # Swapping elements if a smaller value than the pivot
                    # is encountered when going through, where the larger
                    # value is a the index p
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            # Swap the pivot to the middle of the 2 partitions
            nums[p], nums[r] = pivot, nums[p]
            
            # Selecting which half based on partition idx (p)
            if p > k:
                return quick_search(l, p - 1)
            elif p < k:
                return quick_search(p + 1, r)
            else:
                return nums[p]
        
        return quick_search(0, len(nums) - 1)