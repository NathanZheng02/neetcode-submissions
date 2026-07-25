class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Edge Case
        if k == 0:
            return False
        
        window = set()

        # Setup: Input k values into set
        for i in range(k):
            # Check first case
            if nums[i] in window:
                return True

            window.add(nums[i])
        
        # Slide through remaining indicies
        for i in range(k, len(nums)):
            # If duplicate in window, return True
            if nums[i] in window:
                return True
            
            # Else remove last from window and add new
            window.remove(nums[i - k])
            window.add(nums[i])

        # Otherwise no duplicates within k
        return False
            