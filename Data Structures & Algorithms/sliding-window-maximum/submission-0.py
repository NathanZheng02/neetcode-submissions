from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Brute Force: O(k * n)
        '''
        for right in range(len(nums) - k + 1):
            maxi = nums[right]
            for j in range(right, right + k):
                maxi = max(maxi, nums[j])
            res.append(maxi)
            
        return res
        '''
        # Repeated work by checking all values inside sliding window
        # We can use a deque and append values to the queue and
        # if we see a value that is greater than values prior, we
        # remove all values from the queue 

        # We know adding and removing values from queue is O(1)
        # The queue also allow us to pop the first element in, which
        # is the left side of the sliding window.
        res = []
        left = 0
        right = 0
        queue = deque() # We store indices [largest left, smallest right]

        while right < len(nums):
            # Remove values if the rightmost value in queue < current
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()

            queue.append(right)

            # If the largest value in the queue is out of the window, we remove it
            if left > queue[0]:
                queue.popleft()
            
            # Make sure the window is size k to add to result array
            # Increment left to close window
            if right + 1 >= k:
                res.append(nums[queue[0]])
                left += 1
            
            right += 1

        return res
