class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Easy way: HashSet with Runtime O(n) and Space O(n)
        # hs = set()
        # for num in nums:
        #     if num in hs:
        #         return num
        #     else:
        #         hs.add(num)

        # Can we do better? Fast and slow pointers.
        # We create nodes by linking nums[i] to nums[nums[i]]
        fast = 0
        slow = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        start = 0
        while True:
            slow = nums[slow]
            start = nums[start]
            if slow == start:
                return slow
