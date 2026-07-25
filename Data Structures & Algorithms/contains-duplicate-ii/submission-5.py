class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        
        window = set()
        left = 0

        for right in range(len(nums)):
            # If right < k (window size), then we just add
            if right < k:
                if nums[right] in window:
                    return True
                window.add(nums[right])
            else:
                # If in window, then return True
                if nums[right] in window:
                    return True
                # Otherwise pop left value and add right value
                window.remove(nums[left])
                left += 1
                window.add(nums[right])
                

        # Otherwise no duplicates within k
        return False
            